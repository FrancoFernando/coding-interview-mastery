# ============================================================================
# PRACTICE: CONNECTED COMPONENTS  (drills templates/graphs/dfs.py, variant #4)
# ============================================================================
# Fill in the body of `count_components` from scratch. Answer key is one folder
# swap away: templates/graphs/dfs.py — don't peek. When you're done, run
#   python practice/graphs/dfs/count_components.py
# to self-check, then tell me and I'll review your code against the template.
#
# ---------------------------------------------------------------------------
# SPECIFICATION
# ---------------------------------------------------------------------------
# Count the connected components of an undirected graph. One DFS floods one
# component; every not-yet-visited node you have to restart from is one more.
#
# Args:
#   n     : number of nodes, labeled 0 .. n-1.
#   edges : list of (u, v) undirected edges. May be empty.
#
# Returns:
#   int — the number of connected components. (No edges -> n singletons -> n.)
#
# Requirements / things the template cares about:
#   - Build the adjacency list yourself; undirected means BOTH directions.
#   - Recursive DFS inner function; mark visited AS YOU ENTER the call
#     (first line), or a cycle recurses forever.
#   - Outer loop over ALL nodes: a fresh (unvisited) start = a new component.
#
# Example:
#   n = 5, edges = [(0, 1), (1, 2), (3, 4)]
#   -> 2   ({0,1,2} and {3,4})


def count_components(n, edges):
    """n nodes 0..n-1, undirected edges. Returns the number of components."""
    pass


# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
def _run_tests():
    # 1. two components
    assert count_components(5, [(0, 1), (1, 2), (3, 4)]) == 2

    # 2. no edges -> every node is its own component
    assert count_components(4, []) == 4

    # 3. fully connected -> one component
    assert count_components(3, [(0, 1), (1, 2), (2, 0)]) == 1

    # 4. a cycle plus an isolated node (cycle must not loop forever)
    assert count_components(4, [(0, 1), (1, 2), (2, 0)]) == 2

    # 5. edge direction must not matter (undirected both ways)
    assert count_components(3, [(2, 1), (1, 0)]) == 1

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()
