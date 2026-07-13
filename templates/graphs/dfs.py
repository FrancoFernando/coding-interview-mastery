# ============================================================================
# DFS  (Depth-First Search) — recursive and iterative
# ============================================================================
# Explore as deep as possible along each branch, then backtrack. Use for
# "visit/reach everything", connected components, flood fill, reachability, and
# as the skeleton UNDER cycle detection, topological sort, and tree DP.
# DFS does NOT give shortest paths in an unweighted graph — that's BFS.
#
# Trigger words: "connected", "reachable", "flood fill", "count regions/islands",
# "explore all", "surrounded", "path exists" (ANY path, not the shortest).
#
# THE ONE RULE THAT PREVENTS MOST DFS BUGS:
#   mark a node visited AS YOU ENTER it (recursive: first line of the call;
#   iterative: WHEN YOU PUSH, not when you pop). Otherwise a cycle or a
#   re-reachable node sends you into infinite recursion / pushes the same node
#   many times. Same rule as BFS's "mark on enqueue".


# ============================================================================
# 1. RECURSIVE DFS ON A GRAPH  (adjacency list, visited set)  — the default
# ============================================================================
# From a node, recurse into each unvisited neighbor. `visited` both prevents
# infinite loops on cycles and stops re-work. Pre-order: you "see" a node the
# moment you enter it.

def dfs(graph, start):
    """graph: dict node -> list of neighbors. Returns the set of reachable nodes."""
    visited = set()

    def visit(node):
        visited.add(node)                 # mark ON ENTRY
        for nxt in graph[node]:
            if nxt not in visited:
                visit(nxt)

    visit(start)
    return visited


# ============================================================================
# 2. ITERATIVE DFS  (explicit stack) — when recursion depth is a risk
# ============================================================================
# Same traversal without the call stack: push start, then pop-and-expand. Reach
# for this when the graph can be deep enough to blow Python's ~1000 recursion
# limit (a long chain / a big grid).
#
# THE PUSH/POP TRAP: mark visited WHEN YOU PUSH (like BFS enqueue). Mark on pop
# instead and the same node can sit on the stack several times and be processed
# more than once. Neighbors pop in reverse push order — fine for a plain
# traversal; reverse the neighbor loop if you need a specific visit order.

def dfs_iter(graph, start):
    visited = {start}                     # mark on push
    stack = [start]

    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)          # <-- mark HERE, on push
                stack.append(nxt)

    return visited


# ============================================================================
# 3. GRID DFS  (single source) — the graph is implicit
# ============================================================================
# Neighbors are the 4 orthogonal cells; a bounds + passability check replaces
# the adjacency list. Recursive flood fill, mutating the grid as the visited
# marker (O(1) space beyond recursion). The classic "number of islands" atom;
# returning `area` also solves "max area of island".

def dfs_grid(grid, sr, sc):
    rows, cols = len(grid), len(grid[0])
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def visit(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
            return 0                       # out of bounds or not land/passable
        grid[r][c] = 0                     # mark visited by sinking the cell
        area = 1
        for dr, dc in DIRS:
            area += visit(r + dr, c + dc)
        return area

    return visit(sr, sc)                   # size of the component containing (sr, sc)


# ============================================================================
# 4. CONNECTED COMPONENTS  (loop every node as a DFS root) — the payoff
# ============================================================================
# One DFS floods one component. To COUNT (or label) components, start a fresh
# DFS from every not-yet-visited node; each new start = one more component.
# (Union-Find solves the same thing incrementally — see union_find.py.)

def count_components(n, edges):
    """n nodes 0..n-1, undirected edges. Returns the number of components."""
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)                # undirected: both directions

    visited = set()

    def visit(node):
        visited.add(node)
        for nxt in graph[node]:
            if nxt not in visited:
                visit(nxt)

    components = 0
    for node in range(n):
        if node not in visited:           # a fresh start = a new component
            components += 1
            visit(node)

    return components


# ============================================================================
# PRACTICE LADDER  (do them in this order)
# ============================================================================
# Direct use — flood one region / reach everything
#   1. LC 200   Number of Islands       — grid DFS, count fresh starts (templates #3/#4)
#   2. LC 695   Max Area of Island      — grid DFS returning a size
#   3. LC 733   Flood Fill              — grid DFS, repaint as you go
#
# Disguised / sub-step — recognize the trigger
#   4. LC 133   Clone Graph             — DFS with a node->copy dict AS the visited map
#   5. LC 130   Surrounded Regions      — DFS from the BORDER inward to mark the safe cells
#   6. LC 417   Pacific Atlantic Water Flow — two DFS floods, one from each ocean's edges
#
# Harder / where iterative or coloring matters
#   7. LC 207   Course Schedule         — cycle detection via DFS (see topological_sort.py)
#   8. LC 802   Find Eventual Safe States — DFS + 3-color (cross-link: topological_sort.py)
#
# Checkpoint: if you nail 200 -> 133 -> 417, you own this pattern.
