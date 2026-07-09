from collections import deque

# ============================================================================
# PRACTICE: MULTI-SOURCE BFS  (drills templates/graphs/bfs.py, variant #4)
# ============================================================================
# Fill in the body of `multi_source_bfs` from scratch. Answer key is one folder
# swap away: templates/graphs/bfs.py — don't peek. When you're done, run
#   python practice/graphs/bfs/multi_source.py
# to self-check, then tell me and I'll review your code against the template.
#
# ---------------------------------------------------------------------------
# SPECIFICATION
# ---------------------------------------------------------------------------
# Given a grid and a set of source cells, compute the shortest distance (in
# 4-directional steps) from EACH reachable cell to its NEAREST source.
#
# Args:
#   grid    : list[list[int]]. A cell with value 0 is a WALL (impassable);
#             any non-zero value is passable. Sources are always passable.
#   sources : iterable of (r, c) tuples — the starting cells, all at distance 0.
#
# Returns:
#   dist : dict mapping (r, c) -> int, the number of steps from that cell to
#          the nearest source. Every passable cell reachable from any source
#          must appear; walls and unreachable cells must NOT appear.
#
# Requirements / things the template cares about:
#   - Seed ALL sources into the queue up front, each at distance 0.
#   - Expand all fronts in lockstep so the first time a cell is reached, it is
#     reached from its closest source.
#   - Mark a cell visited WHEN YOU ENQUEUE it (not on dequeue).
#   - 4-directional movement.
#
# Example:
#   grid = [[1, 1, 1],
#           [1, 0, 1],
#           [1, 1, 1]]
#   sources = [(0, 0)]
#   -> dist[(0,0)] = 0, dist[(2,2)] = 4, and (1,1) is absent (it's a wall).


def multi_source_bfs(grid, sources):
    """sources: iterable of (r, c) starting cells. Returns dist dict."""
    rows, cols = len(grid), len(grid[0])
    dist = {(r,c) : 0 for (r,c) in sources}
    q = deque([(r,c) for (r,c) in sources])
    DIRS = ((1,0), (-1,0), (0,1), (0,-1))

    while q:
        r, c = q.popleft()
        d = dist[(r,c)]
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in dist and grid[nr][nc]:
                dist[(nr,nc)] = d + 1
                q.append((nr,nc))
    return dist

# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
def _run_tests():
    # 1. single source, no walls
    g1 = [[1, 1], [1, 1]]
    assert multi_source_bfs(g1, [(0, 0)]) == {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 2}

    # 2. single source, a wall in the middle (must route around)
    g2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    d2 = multi_source_bfs(g2, [(0, 0)])
    assert (1, 1) not in d2, "wall must not appear in dist"
    assert d2[(2, 2)] == 4, f"expected 4, got {d2.get((2, 2))}"

    # 3. TWO sources — every cell takes distance to the NEAREST
    g3 = [[1, 1, 1, 1, 1]]
    d3 = multi_source_bfs(g3, [(0, 0), (0, 4)])
    assert d3 == {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 1, (0, 4): 0}, d3

    # 4. an isolated pocket that no source can reach is absent
    g4 = [[1, 0, 1]]
    d4 = multi_source_bfs(g4, [(0, 0)])
    assert d4 == {(0, 0): 0}, d4

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()
