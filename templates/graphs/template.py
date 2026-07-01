from collections import deque

# ============================================================================
# 1. SIMPLE BFS ON A GRAPH  (adjacency list, single source)
# ============================================================================
# Use when: shortest path in an UNWEIGHTED graph, or any "reach all nodes from
# one start" traversal. BFS visits nodes in order of increasing distance, so the
# first time you pop a node you have found its shortest distance from `start`.
#
# THE ONE RULE THAT PREVENTS MOST BFS BUGS:
#   mark a node visited WHEN YOU ENQUEUE it, not when you dequeue it.
#   If you mark on dequeue, the same node gets pushed many times before it is
#   processed -> duplicates in the queue, wrong distances, TLE.

def bfs(graph, start):
    """graph: dict node -> list of neighbors. Returns dist: node -> hops."""
    visited = {start}                 # mark on enqueue
    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)      # <-- mark HERE, on enqueue
                dist[nxt] = dist[node] + 1
                queue.append(nxt)

    return dist


# ============================================================================
# 2. LEVEL-BY-LEVEL BFS  (same skeleton, one extra loop)
# ============================================================================
# Use when you need to know / act on each "layer" as a whole (depth of a layer,
# number of steps, process a full ring at a time). Snapshot len(queue) BEFORE
# the inner loop so you drain exactly the current level.

def bfs_levels(graph, start):
    visited = {start}
    queue = deque([start])
    steps = 0

    while queue:
        for _ in range(len(queue)):   # <-- freeze the size of THIS level
            node = queue.popleft()
            # ... do per-node work for this level ...
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        steps += 1                    # one full level finished

    return steps


# ============================================================================
# 3. GRID BFS  (single source) — the graph is implicit
# ============================================================================
# Neighbors are the 4 orthogonal cells. Same skeleton; the only new thing is
# generating neighbors with the direction arrays and a bounds check.

def bfs_grid(grid, sr, sc):
    rows, cols = len(grid), len(grid[0])
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = {(sr, sc)}
    dist = {(sr, sc): 0}
    queue = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols        # in bounds
                    and (nr, nc) not in visited
                    and grid[nr][nc] != 0):              # passable (problem-specific)
                visited.add((nr, nc))
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))

    return dist


# ============================================================================
# 4. MULTI-SOURCE ("double source") BFS  — the payoff
# ============================================================================
# Use when the question is "shortest distance FROM THE NEAREST of several
# sources" (nearest gate, nearest 0, minutes until ALL oranges rot, etc.).
#
# THE ONLY CHANGE from single-source BFS: seed the queue with EVERY source at
# once and mark them all visited at distance 0. BFS then expands all fronts in
# lockstep, so the first time any cell is reached, it is reached from its
# CLOSEST source. That is the whole trick — no per-source loop, no re-running.

def multi_source_bfs(grid, sources):
    """sources: iterable of (r, c) starting cells."""
    rows, cols = len(grid), len(grid[0])
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    dist = {}
    for r, c in sources:              # <-- seed ALL sources up front
        dist[(r, c)] = 0
        queue.append((r, c))

    while queue:                      # identical loop body to single-source
        r, c = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in dist
                    and grid[nr][nc] != 0):
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))

    return dist


# ============================================================================
# 5. MULTI-SOURCE BFS, level counting  (e.g. LC 994 Rotting Oranges)
# ============================================================================
# "How many rounds until everything is filled/rotten?" = number of BFS levels
# minus one. Track a `fresh` count to detect the unreachable case.

def rotting_oranges(grid):
    rows, cols = len(grid), len(grid[0])
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:       # every rotten cell is a source
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue and fresh:            # stop early once nothing fresh remains
        for _ in range(len(queue)):   # level-by-level = one minute per level
            r, c = queue.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # mark on enqueue (mutate grid as visited)
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1

    return -1 if fresh else minutes   # leftover fresh => unreachable
