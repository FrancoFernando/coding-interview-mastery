from collections import deque

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
    


# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
def _is_valid_topo(order, n, edges):
    if order is None or sorted(order) != list(range(n)):
        return False                       # must be a permutation of 0..n-1
    pos = {node: i for i, node in enumerate(order)}
    return all(pos[u] < pos[v] for u, v in edges)   # every edge points forward


def _run_tests():
    # 1. simple diamond — several valid orders exist
    assert _is_valid_topo(topo_kahn(4, [(0, 1), (0, 2), (1, 3), (2, 3)]),
                          4, [(0, 1), (0, 2), (1, 3), (2, 3)])

    # 2. straight chain — exactly one valid order
    assert topo_kahn(3, [(0, 1), (1, 2)]) == [0, 1, 2]

    # 3. no edges — any permutation is fine, must contain all nodes
    assert sorted(topo_kahn(3, [])) == [0, 1, 2]

    # 4. two-node cycle -> None
    assert topo_kahn(2, [(0, 1), (1, 0)]) is None

    # 5. cycle buried in a larger graph -> None
    assert topo_kahn(4, [(0, 1), (1, 2), (2, 1), (2, 3)]) is None

    # 6. self-loop is a cycle -> None
    assert topo_kahn(1, [(0, 0)]) is None

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()
