# Shared self-check for topological-sort drills whose contract is
# "return a valid topo order, or None on a cycle" — i.e. kahn.py and dfs.py.
# The check validates the CONTRACT, not the algorithm, so both variants reuse it.
#
# NOT shared by kahn_smallest.py: that variant has a stronger contract (the
# lexicographically smallest order), so it asserts exact equality on its own.

def _is_valid_topo(order, n, edges):
    if order is None or sorted(order) != list(range(n)):
        return False                       # must be a permutation of 0..n-1
    pos = {node: i for i, node in enumerate(order)}
    return all(pos[u] < pos[v] for u, v in edges)   # every edge points forward


def run_tests(topo):
    """topo: a function (n, edges) -> order | None. Runs the shared contract."""
    # 1. simple diamond — several valid orders exist
    assert _is_valid_topo(topo(4, [(0, 1), (0, 2), (1, 3), (2, 3)]),
                          4, [(0, 1), (0, 2), (1, 3), (2, 3)])

    # 2. straight chain — the topo order is UNIQUE, so exact match is contractual
    assert topo(3, [(0, 1), (1, 2)]) == [0, 1, 2]

    # 3. no edges — any permutation is fine, must contain all nodes
    assert sorted(topo(3, [])) == [0, 1, 2]

    # 4. two-node cycle -> None
    assert topo(2, [(0, 1), (1, 0)]) is None

    # 5. cycle buried in a larger graph -> None
    assert topo(4, [(0, 1), (1, 2), (2, 1), (2, 3)]) is None

    # 6. self-loop is a cycle -> None
    assert topo(1, [(0, 0)]) is None

    print("All tests passed ✅")
