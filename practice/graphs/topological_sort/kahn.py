from collections import deque
from enum import Enum

# ============================================================================
# PRACTICE: TOPOLOGICAL SORT — KAHN'S ALGORITHM
#           (drills templates/graphs/topological_sort.py, variant #1)
# ============================================================================
# Fill in the body of `topo_kahn` from scratch. Answer key is one folder swap
# away: templates/graphs/topological_sort.py — don't peek. When you're done, run
#   python practice/graphs/topological_sort/kahn.py
# to self-check, then tell me and I'll review your code against the template.
#
# ---------------------------------------------------------------------------
# SPECIFICATION
# ---------------------------------------------------------------------------
# Return a topological order of a directed graph via Kahn's algorithm (BFS on
# in-degrees), or None if the graph has a cycle (no valid order exists).
#
# Args:
#   n     : int. Nodes are labelled 0 .. n-1.
#   edges : list[(u, v)]. Each edge means u MUST come before v (u is a
#           prerequisite of v).
#
# Returns:
#   order : list[int] — a permutation of 0..n-1 where, for every edge (u, v),
#           u appears before v. Any valid order is accepted.
#           Return None if the graph contains a directed cycle.
#
# Requirements / things the template cares about:
#   - Build an in-degree array; seed the queue with EVERY in-degree-0 node
#     (this is multi-source BFS).
#   - When you place a node, decrement each neighbor's in-degree; a neighbor
#     that hits 0 is now free — enqueue it.
#   - Cycle detection is FREE: if you placed fewer than n nodes, the leftovers
#     are stuck in a cycle -> return None.
#
# Example:
#   n = 4, edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
#   -> 0 before 1 and 2; 1 and 2 before 3.  e.g. [0, 1, 2, 3] or [0, 2, 1, 3].
#   n = 2, edges = [(0, 1), (1, 0)]  -> None (cycle).


def topo_kahn(n, edges):
    """n nodes 0..n-1. edges: (u, v) means u before v. Returns order or None."""
    indegree = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]
    for u, v in edges:
        indegree[v] += 1
        graph[u].append(v)
    
    q = deque(idx for idx, val in enumerate(indegree) if val == 0)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for adj in graph[node]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                q.append(adj)
    return None if len(result) != n else result
    


# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
from _check import run_tests   # shared contract check (see _check.py)

if __name__ == "__main__":
    run_tests(topo_kahn)
