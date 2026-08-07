# ============================================================================
# PRACTICE: GRID DFS  (drills templates/graphs/dfs.py, variant #3)
# ============================================================================
# Fill in the body of `dfs_grid` from scratch. Answer key is one folder swap
# away: templates/graphs/dfs.py — don't peek. When you're done, run
#   python practice/graphs/dfs/grid_area.py
# to self-check, then tell me and I'll review your code against the template.
#
# ---------------------------------------------------------------------------
# SPECIFICATION
# ---------------------------------------------------------------------------
# Flood the connected region of 1-cells containing (sr, sc) and return its
# area. The graph is implicit: neighbors are the 4 orthogonal cells.
#
# Args:
#   grid   : list[list[int]]. 1 = land/passable, anything else = water/wall.
#            You MAY mutate the grid (that's the point — see below).
#   sr, sc : the starting cell. May be water — then the answer is 0.
#
# Returns:
#   int — the number of cells in the connected 1-region containing (sr, sc).
#
# Requirements / things the template cares about:
#   - Mark a cell visited AS YOU ENTER it — sink it (grid[r][c] = 0) so no
#     separate visited set is needed.
#   - Bounds check + passability check REPLACE the adjacency list; doing them
#     at the top of the call keeps the recursion body to one pattern.
#   - 4-directional movement.
#
# Example:
#   grid = [[1, 1, 0],
#           [1, 0, 1]]
#   dfs_grid(grid, 0, 0) -> 3   (the L-shaped region; the lone (1,2) is not it)


def dfs_grid(grid, sr, sc):
    """Returns the area of the connected 1-region containing (sr, sc)."""
    pass


# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
def _run_tests():
    # 1. one solid block
    g1 = [[1, 1], [1, 1]]
    assert dfs_grid(g1, 0, 0) == 4

    # 2. L-shaped region, separate cell excluded
    g2 = [[1, 1, 0], [1, 0, 1]]
    assert dfs_grid(g2, 0, 0) == 3
    assert g2[1][2] == 1, "the other region must be untouched"

    # 3. start on water -> 0
    g3 = [[0, 1], [1, 1]]
    assert dfs_grid(g3, 0, 0) == 0

    # 4. snake — forces deep backtracking, no diagonal cheating
    g4 = [[1, 0, 1],
          [1, 0, 1],
          [1, 1, 1]]
    assert dfs_grid(g4, 0, 0) == 7

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()
