from collections import deque

# ============================================================================
# TOPOLOGICAL SORT
# ============================================================================
# A topological order of a DIRECTED graph is a linear ordering of nodes such
# that every edge u -> v puts u before v. It exists IFF the graph is a DAG
# (no directed cycle). Use when the problem says "prerequisites", "must come
# before", "build order", "dependency", "can you finish all tasks".
#
# Two ways to produce it. Learn Kahn's first — it doubles as cycle detection
# and is just multi-source BFS seeded on the in-degree-0 nodes.


# ============================================================================
# 1. KAHN'S ALGORITHM  (BFS, in-degree)  — the default
# ============================================================================
# Idea: a node can go next only once all its prerequisites are placed, i.e.
# when its in-degree drops to 0. Seed the queue with every in-degree-0 node
# (multi-source BFS!), and each time you place a node, "remove" its outgoing
# edges by decrementing neighbors' in-degrees; any that hit 0 join the queue.
#
# CYCLE DETECTION IS FREE: if the final order has fewer than n nodes, the
# leftover nodes are locked in a cycle (their in-degree never reached 0).

def topo_kahn(n, edges):
    """n nodes labelled 0..n-1. edges: list of (u, v) meaning u must come before v.
       Returns a valid order, or None if the graph has a cycle."""
    graph = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1                     # v depends on u

    queue = deque(i for i in range(n) if indeg[i] == 0)   # seed ALL sources
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indeg[nxt] -= 1               # drop the edge node -> nxt
            if indeg[nxt] == 0:           # nxt now has all prereqs placed
                queue.append(nxt)

    return order if len(order) == n else None   # short order => cycle


# ============================================================================
# 2. DFS VARIANT  (post-order, then reverse)
# ============================================================================
# Idea: a node's dependents must all be emitted before it, so append a node to
# the output AFTER its DFS fully returns (post-order). That yields REVERSE
# topological order; reverse it (or build with appendleft) at the end.
#
# CYCLE DETECTION uses 3 colors:
#   WHITE = unvisited, GRAY = on the current recursion stack, BLACK = done.
#   Hitting a GRAY node means an edge back into the active path -> a cycle.

WHITE, GRAY, BLACK = 0, 1, 2

def topo_dfs(n, edges):
    """Returns a valid order, or None if the graph has a cycle."""
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    color = [WHITE] * n
    order = deque()                       # appendleft = build in correct order
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        color[node] = GRAY                # entering: mark on the stack
        for nxt in graph[node]:
            if color[nxt] == GRAY:        # back-edge into active path
                has_cycle = True
                return
            if color[nxt] == WHITE:
                dfs(nxt)
                if has_cycle:
                    return
        color[node] = BLACK               # leaving: fully processed
        order.appendleft(node)            # post-order, reversed on the fly

    for i in range(n):
        if color[i] == WHITE:
            dfs(i)
            if has_cycle:
                return None

    return list(order)


# ============================================================================
# 3. LEXICOGRAPHICALLY SMALLEST ORDER  (Kahn's + heap)
# ============================================================================
# When ties must break to the smallest label, swap the plain queue for a
# min-heap. Same algorithm, O(n log n) instead of O(n).

import heapq

def topo_kahn_smallest(n, edges):
    graph = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1

    heap = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(heap)
    order = []

    while heap:
        node = heapq.heappop(heap)        # smallest available label
        order.append(node)
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(heap, nxt)

    return order if len(order) == n else None


# ============================================================================
# PRACTICE LADDER  (do them in this order)
# ============================================================================
# Cycle detection first — topo sort with the order thrown away
#   1. LC 207   Course Schedule — "can you finish?" = does a topo order exist
#   2. LC 802   Find Eventual Safe States — DFS coloring / reverse-graph Kahn's
#
# Produce the actual order
#   3. LC 210   Course Schedule II — return any valid order (Kahn's, direct)
#   4. LC 310   Minimum Height Trees — peel in-degree-1 leaves layer by layer
#               (topo-flavored multi-source BFS on an undirected graph)
#
# Disguised / harder
#   5. LC 269   Alien Dictionary — BUILD the edges from adjacent words, then topo
#   6. LC 1136  Parallel Courses — answer is the number of BFS levels (longest chain)
#   7. LC 2115  Find All Possible Recipes from Given Supplies — topo over recipes
#
# Checkpoint: if you nail 207 -> 210 -> 269, you own this pattern.
