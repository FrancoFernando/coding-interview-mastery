# Muscle-Memory Primitives for Coding Interviews

A curated checklist of techniques to drill until they're automatic. Star (**★**) marks the must-haves — the ones to nail before anything else, since they cover roughly 70% of medium-tagged interview problems and are building blocks for the rest.

---

## Graph & tree traversal

- **★ BFS on a graph** with `visited` set / array
- **★ Recursive DFS on a graph** with `visited`
- **★ Iterative DFS** (explicit stack) — needed when recursion limit is a concern
- **★ Grid BFS/DFS** with `dx = [-1,0,1,0]`, `dy = [0,1,0,-1]` and bounds check
- **★ Level-by-level BFS** (for shortest path / "depth of layer" problems)
- **★ Tree DFS returning `(depth, parent)` arrays**
- **★ Tree post-order DP** (return a summary up from each child, combine at parent)
- Topological sort — Kahn's (BFS, in-degree) and DFS variant
- Cycle detection (white/gray/black coloring in DFS)
- Tree diameter (two BFS, or one DFS returning two heights)
- Dijkstra (heap-based)
- Bellman-Ford (when negative edges)
- LCA via binary lifting

---

## Binary search

- **★ Standard binary search** on a sorted array
- **★ `bisect_left` / `bisect_right`** (lower/upper bound — know which to reach for)
- **★ Binary search on the answer**: define a predicate `feasible(x)`, find smallest/largest feasible — this pattern is everywhere at senior level

---

## Data structures

- **★ Union-Find** with path compression + union by rank
- **★ Heap** (min-heap is default; for max-heap, negate values in Python)
- **★ Top-k with heap** (heap of size k, pop on overflow)
- **★ Monotonic stack** (next greater/smaller element)
- **★ Monotonic deque** (sliding window max/min)
- **★ Hash map for counting** + the `Counter` patterns (most-frequent, anagram, etc.)
- Two heaps for running median
- Trie (insert / search / prefix-walk)
- Fenwick tree (BIT) — prefix sums with point updates
- Segment tree — range query + range update
- Sparse table — `O(1)` range min/max on static array

---

## Strings

- **★ Sliding window with hash map** (longest substring with property X)
- **★ Two pointers** (palindromes, partitioning)
- KMP failure function
- Rolling hash (Rabin-Karp pattern)
- Z-function (similar use cases to KMP, easier to remember)

---

## Dynamic programming

- **★ 1D DP scan** (climbing stairs / house robber family)
- **★ 2D grid DP** (paths, edit distance, LCS, knapsack pattern)
- **★ 0/1 knapsack and unbounded knapsack** (both directions of the inner loop)
- **★ DP on trees** (post-order, two states at each node — "include / exclude")
- Interval DP (length increasing — palindrome partitioning, MCM)
- Bitmask DP (small `n <= 20` — TSP, assignment problems)
- Digit DP (for "count numbers <= N satisfying property")

---

## Math & number theory

- **★ Modular exponentiation** — `pow(a, b, MOD)`
- **★ GCD** (Euclidean) and LCM (`a*b // gcd`)
- **★ Sieve of Eratosthenes** (primes up to `n`)
- Modular inverse via Fermat's little theorem (`pow(a, MOD-2, MOD)`)
- Precomputed factorials + inverse factorials -> `nCr mod p` in `O(1)`

---

## Bit manipulation

- **★ Iterate over set bits**: `while x: low = x & -x; ...; x -= low`
- **★ Count set bits**: `bin(x).count('1')` or `x.bit_count()` in 3.10+
- **★ Power-of-2 check**: `x > 0 and x & (x-1) == 0`
- **★ Toggle / set / clear bit `i`**: `x ^ (1<<i)`, `x | (1<<i)`, `x & ~(1<<i)`
- Iterate over all subsets of a bitmask `m`: `s = m; while s: ...; s = (s-1) & m`

---

## Two pointers & intervals

- **★ Two pointers on sorted arrays** (2-sum, 3-sum)
- **★ Fast/slow pointers** (cycle detection, find middle)
- **★ Merge intervals** (sort by start, sweep)
- Line sweep / event-based scan (start/end events sorted by time)

---

## Sorting & selection

- **★ Built-in sort with a key/comparator** (custom `key=`, `functools.cmp_to_key`)
- Quickselect for k-th smallest in `O(n)` expected
- Counting sort / bucket sort (when value range is small)

---

## Misc patterns worth a spot in muscle memory

- **★ Backtracking template** (permutations, combinations, subsets, N-queens)
- **★ Recursion + memoization** (`@lru_cache` for top-down DP)
- Reservoir sampling (k = 1 case is one line — useful for streaming problems)
- Difference arrays (range updates in `O(1)` each, prefix-sum at the end)

---

## How to actually grind this

Don't try to learn it all at once. Pick **one primitive a week**. For each:

1. **Day 1**: read the canonical implementation, type it once.
2. **Day 2-3**: solve 2-3 LeetCode problems that *directly* use it (no fancy variation).
3. **Day 4-5**: 2-3 problems that use it as a *sub-step* (you have to recognize the trigger).
4. **End of week**: type it from blank canvas, no reference. If you get stuck, restart from the canonical version and try again.

Nail the **★** items first. Once those are automatic, the rest stop feeling like "new techniques" and start feeling like "another variation on a thing I already know."
