# ============================================================================
# UNION-FIND  (Disjoint Set Union, DSU)
# ============================================================================
# Maintains a partition of elements into disjoint sets under two operations:
#   find(x)     -> the representative ("root") of x's set
#   union(a, b) -> merge the two sets containing a and b
# Both run in ~O(1) amortized (inverse-Ackermann) with the two optimizations
# below. Use when the problem is about GROUPING or CONNECTIVITY in an
# *undirected* graph and you don't need actual paths: connected components,
# "are a and b in the same group", cycle detection, Kruskal's MST.
#
# Trigger words: "connected", "components", "groups", "provinces", "friend
# circles", "merge accounts", "same network", "redundant edge", "islands".
# If the question needs a shortest path or the path itself, reach for BFS/DFS
# instead — DSU only knows WHICH set, never the route.
#
# THE ONE RULE THAT PREVENTS MOST DSU BUGS:
#   ALWAYS operate on ROOTS. Call find() on BOTH endpoints before you union or
#   compare them -- never link or test the raw elements. Skipping find() links a
#   node into the wrong tree and silently corrupts every later query.
#   (Second rule: keep BOTH optimizations -- path compression in find AND
#   union by rank/size -- or trees degrade to O(n) chains and you TLE.)


# ============================================================================
# 1. CANONICAL DSU  (path compression + union by rank)  — the workhorse
# ============================================================================
# `parent[x]` points one step toward the root; a root points at itself.
# find() flattens the path (compression); union() hangs the shorter tree under
# the taller one (by rank) so trees stay shallow. `count` tracks how many
# disjoint sets remain -- the answer to most "number of components" problems.

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))      # every node starts as its own root
        self.rank = [0] * n               # upper bound on each tree's height
        self.count = n                    # number of disjoint sets

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path-halving compress
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)   # <-- ROOTS first, always
        if ra == rb:
            return False                  # already one set -> nothing merged
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra               # ensure ra is the taller root
        self.parent[rb] = ra              # hang shorter tree under taller
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1            # equal heights -> result grew by 1
        self.count -= 1                   # two sets became one
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


# ============================================================================
# 2. UNION BY SIZE  (when you need the SIZE of a component)
# ============================================================================
# Same skeleton as #1, but track set sizes instead of rank. Union by size is
# just as good asymptotically AND gives you the answer to "largest connected
# group" for free: size[find(x)] is the size of x's set. Reach for this variant
# the moment the question asks "how big" rather than "how many".

class DSUSize:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n               # size of the tree rooted at each node
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra               # ra is the bigger set
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]    # bigger set absorbs the smaller
        self.count -= 1
        return True

    def set_size(self, x):
        return self.size[self.find(x)]    # size of x's whole component


# ============================================================================
# 3. CYCLE DETECTION / REDUNDANT EDGE  (the payoff of union's return value)
# ============================================================================
# In an UNDIRECTED graph, adding edge (u, v) closes a cycle exactly when u and v
# are ALREADY in the same set. So DSU.union returning False = "this edge is
# redundant". This is the acceptance test inside Kruskal's MST and the whole
# answer to "find the redundant connection". Reuses the canonical DSU verbatim.

def has_cycle_undirected(n, edges):
    """n nodes 0..n-1. Returns True if the edges contain a cycle."""
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):           # u, v already connected -> cycle
            return True
    return False


# ============================================================================
# 4. NON-INTEGER ELEMENTS  (dict-backed DSU for strings / grid coords)
# ============================================================================
# When elements aren't 0..n-1 integers -- email strings, (r, c) grid cells,
# variable names -- back `parent` with a dict instead of a list and create
# nodes lazily. Everything else is identical. Use for accounts-merge, equation
# groups, or islands keyed by coordinate without flattening to indices first.

class DSUDict:
    def __init__(self):
        self.parent = {}                  # element -> parent element
        self.count = 0                    # distinct sets seen so far

    def add(self, x):
        if x not in self.parent:          # first sighting -> its own root
            self.parent[x] = x
            self.count += 1

    def find(self, x):
        self.add(x)                       # tolerate unseen elements
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra              # (no rank here for brevity; add if hot)
        self.count -= 1
        return True


# ============================================================================
# PRACTICE LADDER  (do them in this order)
# ============================================================================
# Direct use — count components with the canonical DSU
#   1. LC 547   Number of Provinces        — build DSU from the matrix, read count
#   2. LC 323   Number of Connected Components in an Undirected Graph — same idea
#
# Disguised / sub-step — recognize the trigger
#   3. LC 684   Redundant Connection       — union returns False => THE cycle edge
#   4. LC 990   Satisfiability of Equality Equations — union all '==', then scan
#               '!=' for a contradiction (both endpoints already same root)
#   5. LC 200   Number of Islands          — grid DSU: union adjacent land cells
#
# Payoff / harder
#   6. LC 721   Accounts Merge             — dict/string DSU (template #4)
#   7. LC 305   Number of Islands II       — dynamic DSU: add land, count changes
#   8. LC 1319  Number of Operations to Make Network Connected — (components-1)
#               cables needed vs. spare edges available
#
# Checkpoint: if you nail 547 -> 684 -> 721, you own this pattern.
