# ============================================================================
# PRACTICE: ITERATIVE DFS  (drills templates/graphs/dfs.py, variant #2)
# ============================================================================
# Fill in the body of `dfs_iter` from scratch. Answer key is one folder swap
# away: templates/graphs/dfs.py — don't peek. When you're done, run
#   python practice/graphs/dfs/iterative.py
# to self-check, then tell me and I'll review your code against the template.
#
# ---------------------------------------------------------------------------
# SPECIFICATION
# ---------------------------------------------------------------------------
# DFS with an explicit stack instead of recursion — the variant you reach for
# when the graph is deep enough to blow Python's ~1000-frame recursion limit.
#
# Args:
#   graph : dict node -> list of neighbors (directed edges as given).
#   start : the starting node. Always a key of `graph`.
#
# Returns:
#   set of all nodes reachable from `start` (including `start` itself).
#
# Requirements / things the template cares about:
#   - Mark a node visited WHEN YOU PUSH it (like BFS's mark-on-enqueue), NOT
#     when you pop. Mark on pop and the same node can sit on the stack several
#     times — the self-check's deep-chain test will blow up on that via the
#     diamond test's duplicate pushes.
#   - No recursion at all: the last test is a 10,000-node chain.
#
# Example:
#   graph = {"a": ["b", "c"], "b": ["d"], "c": [], "d": []}
#   dfs_iter(graph, "a") -> {"a", "b", "c", "d"}


def dfs_iter(graph, start):
    """graph: dict node -> list of neighbors. Returns the set of reachable nodes."""
    pass


# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
def _run_tests():
    # 1. reaches everything, ignores the unreachable
    g1 = {"a": ["b", "c"], "b": ["d"], "c": [], "d": [], "z": ["a"]}
    assert dfs_iter(g1, "a") == {"a", "b", "c", "d"}, "z is unreachable from a"

    # 2. cycle must terminate
    g2 = {0: [1], 1: [2], 2: [0]}
    assert dfs_iter(g2, 0) == {0, 1, 2}

    # 3. diamond — b and c both point at d; mark-on-pop pushes d twice
    g3 = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}
    assert dfs_iter(g3, "a") == {"a", "b", "c", "d"}

    # 4. 10,000-node chain — recursion would exceed the interpreter limit
    n = 10_000
    g4 = {i: [i + 1] for i in range(n)}
    g4[n] = []
    assert len(dfs_iter(g4, 0)) == n + 1

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()
