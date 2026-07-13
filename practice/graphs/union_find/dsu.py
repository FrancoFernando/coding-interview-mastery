# ============================================================================
# PRACTICE: UNION-FIND — CANONICAL DSU  (path compression + union by rank)
#           (drills templates/graphs/union_find.py, variant #1)
# ============================================================================
# Fill in the methods of `DSU` from scratch. Answer key is one folder swap away:
# templates/graphs/union_find.py — don't peek. When you're done, run
#   python practice/graphs/union_find/dsu.py
# to self-check, then tell me and I'll review your code against the template.
#
# ---------------------------------------------------------------------------
# SPECIFICATION  (the self-check depends on this exact interface)
# ---------------------------------------------------------------------------
# A disjoint-set structure over integer elements 0 .. n-1.
#
#   __init__(n)      : n singleton sets {0}, {1}, ..., {n-1}. Expose a `count`
#                      attribute = number of disjoint sets (starts at n).
#   find(x)  -> root : the representative of x's set. Apply PATH COMPRESSION so
#                      repeated finds get flatter/faster.
#   union(a, b) -> bool : merge the sets of a and b. Return True if they were
#                      separate (a real merge happened), False if already
#                      together. Attach by RANK (or size) so trees stay shallow.
#                      Decrement `count` on every real merge.
#   connected(a, b) -> bool : True iff a and b are in the same set.
#
# Requirements / things the template cares about:
#   - ALWAYS operate on ROOTS: call find() on both endpoints before you union
#     or compare — never link/test the raw elements. (THE ONE DSU RULE.)
#   - Keep BOTH optimizations (compression in find + rank/size in union) or the
#     trees degrade to O(n) chains.
#
# Example:
#   d = DSU(4); d.union(0, 1); d.union(2, 3)
#   d.connected(0, 1)  -> True
#   d.connected(1, 2)  -> False
#   d.union(0, 1)      -> False   (already one set)
#   d.count            -> 2       ({0,1}, {2,3})


class DSU:
    def __init__(self, n):
        # TODO: parent, rank (or size), and count
        pass

    def find(self, x):
        # TODO: return root of x, with path compression
        pass

    def union(self, a, b):
        # TODO: merge by rank/size; return True on a real merge, else False
        pass

    def connected(self, a, b):
        # TODO
        pass


# ============================================================================
# SELF-CHECK  (don't edit below this line)
# ============================================================================
def _run_tests():
    # 1. fresh structure: n singleton sets
    d = DSU(5)
    assert d.count == 5
    assert not d.connected(0, 1)

    # 2. union returns True on a real merge, False when already joined
    assert d.union(0, 1) is True
    assert d.union(1, 2) is True
    assert d.union(0, 2) is False          # 0 and 2 already in one set
    assert d.count == 3                     # {0,1,2}, {3}, {4}

    # 3. connectivity is transitive
    assert d.connected(0, 2)                # via 1
    assert not d.connected(0, 3)

    # 4. count reaches 1 once everything is merged
    d.union(3, 4)
    d.union(2, 4)
    assert d.count == 1
    assert all(d.connected(0, i) for i in range(5))

    # 5. a longer chain still finds a single root (compression must not corrupt)
    e = DSU(6)
    for i in range(5):
        e.union(i, i + 1)                   # 0-1-2-3-4-5 in a line
    root = e.find(0)
    assert all(e.find(i) == root for i in range(6))
    assert e.count == 1

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()
