from collections import deque

# ============================================================================
# PRACTICE: TOPOLOGICAL SORT — DFS POST-ORDER (3-color)
#           (drills templates/graphs/topological_sort.py, variant #2)
# ============================================================================
# Fill in the body of `topo_dfs` from scratch. Answer key is one folder swap
# away: templates/graphs/topological_sort.py — don't peek. When you're done, run
#   python practice/graphs/topological_sort/dfs.py
# to self-check, then tell me and I'll review your code against the template.
#
# ---------------------------------------------------------------------------
# SPECIFICATION  (same contract as kahn.py — different mechanism)
# ---------------------------------------------------------------------------
# Return a topological order of a directed graph via DFS post-order, or None if
# the graph has a cycle.
#
# Args:
#   n     : int. Nodes are labelled 0 .. n-1.
#   edges : list[(u, v)]. Each edge means u MUST come before v.
#
# Returns:
#   order : list[int] — a permutation of 0..n-1 with every edge (u, v) forward.
#           Any valid order is accepted. Return None on a directed cycle.
#
# Requirements / things the template cares about:
#   - POST-ORDER: append a node only AFTER its DFS fully returns. That produces
#     REVERSE topological order — reverse it at the end (or appendleft as you go).
#   - CYCLE DETECTION via 3 colors:
#       WHITE = unvisited, GRAY = on the current recursion stack, BLACK = done.
#     Reaching a GRAY node = a back-edge into the active path = a cycle -> None.
#     (A GRAY hit is the cycle signal; a BLACK hit is just an already-finished
#     node — NOT a cycle. Getting that distinction right is the whole lesson.)
#   - Loop over all nodes as DFS roots — the graph may be disconnected.
#
# Example:
#   n = 4, edges = [(0, 1), (0, 2), (1, 3), (2, 3)]  -> e.g. [0, 2, 1, 3]
#   n = 2, edges = [(0, 1), (1, 0)]                  -> None (cycle).

WHITE, GRAY, BLACK = 0, 1, 2


def topo_dfs(n, edges):
    """n nodes 0..n-1. edges: (u, v) means u before v. Returns order or None."""
    # TODO: implement
    pass


# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
from _check import run_tests   # shared contract check (see _check.py)

if __name__ == "__main__":
    run_tests(topo_dfs)
