# 3161. Block Placement Queries

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/block-placement-queries/)

## Problem Description

There is an infinite number line starting at 0 and extending in the positive direction. You process a sequence of queries of two kinds:

- `[1, x]` — place an **obstacle** at position `x` (it is guaranteed no obstacle exists there yet).
- `[2, x, sz]` — answer whether a **block of length `sz`** can be placed somewhere inside `[0, x]` without intersecting any obstacle. The block can *touch* obstacles but not cross them. The block is not actually placed; type-2 queries are independent.

Return a list of booleans, one per type-2 query.

---

## Step 1 — Translate the problem into plain English

Forget the formal wording. You have a number line, and over time people either:

- **Plant a flag** (obstacle) at some position, OR
- **Ask**: "If I had a stick of length `sz`, could I lay it flat somewhere between 0 and `x` *without crossing any flag*?" (touching is fine)

Each type-2 query is independent — nothing is actually placed.

## Step 2 — Reframe: what are we *really* asking?

Picture the obstacles inside `[0, x]` as fence posts. They cut `[0, x]` into a few **gaps**. The stick fits if **any one gap** is `≥ sz`.

So the real question becomes:

> What is the **largest gap** between consecutive obstacles in `[0, x]`?

If `max_gap ≥ sz` → `true`. Otherwise → `false`.

Two edge gaps to keep in mind:

- The gap from **0** to the first obstacle
- The gap from the **last obstacle ≤ x** to **x itself** (the "tail")

## Step 3 — Naive idea (and why it's too slow)

For each type-2 query:

1. Collect all obstacles ≤ x
2. Sort them
3. Walk through and compute gaps
4. Return whether the max gap is ≥ sz

This is `O(n)` per query → `O(n²)` overall. For `n ≈ 10⁵`, too slow. We need to make queries faster.

## Step 4 — Identify the two things we keep recomputing

Every type-2 query needs:

- **(A)** The position of the **largest obstacle ≤ x** — call it `last`. Then `x - last` is the tail gap.
- **(B)** The **maximum gap** among consecutive obstacles in `[0, last]`.

Answer = `max((A's tail gap), (B)) ≥ sz`.

We need data structures that make (A) and (B) fast.

## Step 5 — Pick the right tools

- **For (A) — predecessor of x**: a **sorted set** (Python's `SortedList`). Predecessor lookup is `O(log n)`.
- **For (B) — max gap in a range of positions**: a **segment tree** indexed by position, storing gap values, supporting range-max queries.

The key creative leap: **index the segment tree by coordinate on the number line**, not by query index.

## Step 6 — How we store gaps in the segment tree

Convention: at position `p` we store

```
gap[p] = p − (previous obstacle position)
```

i.e. the gap *ending* at `p`. Treat position 0 as a virtual obstacle so there's always a previous to subtract from.

**Inserting a new obstacle at `p`:**

1. Find `prev` (predecessor) and `next` (successor) in the sorted set.
2. Set `gap[p] = p − prev`.
3. Update `gap[next] = next − p` — the old gap ending at `next` used to span `prev → next`; now it spans `p → next`.

Two point updates per insertion. `O(log n)`.

**Answering query `[2, x, sz]`:**

1. `last` = predecessor of `x` (or 0).
2. `tail = x − last`.
3. `best_inside` = segment tree range max over positions `(0, last]`.
4. Return `max(best_inside, tail) ≥ sz`.

## Step 7 — Trace through the LeetCode example

`queries = [[1,2], [2,3,3], [2,3,1], [2,2,2]]`

Start: `obstacles = {0}` (virtual), all gaps 0.

**[1, 2]** → insert obstacle at 2. `prev = 0`, no next yet. `gap[2] = 2`.
State: `obstacles = {0, 2}`, gaps: `gap[2] = 2`.

**[2, 3, 3]**: x = 3, sz = 3.
- `last` = predecessor of 3 = 2.
- `tail` = 3 − 2 = 1.
- `best_inside` = max gap in `(0, 2]` = 2.
- max(2, 1) = 2. Is 2 ≥ 3? **false** ✓

**[2, 3, 1]**: x = 3, sz = 1.
- Same `last = 2`, `tail = 1`, `best_inside = 2`.
- max = 2 ≥ 1? **true** ✓

**[2, 2, 2]**: x = 2, sz = 2.
- `last` = predecessor ≤ 2 = 2.
- `tail` = 2 − 2 = 0.
- `best_inside` = max gap in `(0, 2]` = 2.
- max(2, 0) = 2 ≥ 2? **true** ✓

Output: `[false, true, true]` ✓

---

## Segment Trees from Scratch

### The motivating question

Suppose you have an array of numbers:

```
index:  0   1   2   3   4   5   6   7
value:  3   1   4   1   5   9   2   6
```

You'll get many queries of two kinds:

- **Update**: "change the value at index 3 to 10"
- **Range query**: "what's the max value between index 2 and index 6?"

Naive: update is O(1), range query is O(n). Over many queries, too slow. Goal: both in **O(log n)**.

### The core idea: precompute answers for chunks

Cache the max for *halves*, then *quarters*, then *eighths* of the array. For any range, stitch the answer together from a handful of precomputed chunks.

```
                    [max of all 8] = 9
                   /                  \
            [max 0..3]=4         [max 4..7]=9
            /        \            /         \
        [0..1]=3  [2..3]=4    [4..5]=9   [6..7]=6
         /  \      /  \        /  \       /  \
        3    1    4    1      5    9     2    6
       (0) (1)  (2)  (3)    (4)  (5)   (6)  (7)
```

Each **internal node** stores the max of its range. Each **leaf** is one array element. Tree height ≈ log₂(n).

### How a range query works

Say you want max of indices `[2, 6]`:

- Root covers `[0, 7]`. Partial overlap → recurse into both children.
- Left child covers `[0, 3]`. Partial overlap → recurse.
  - `[0, 1]` no overlap → skip.
  - `[2, 3]` fully inside → use cached value (4). ✓
- Right child covers `[4, 7]`. Partial overlap → recurse.
  - `[4, 5]` fully inside → 9. ✓
  - `[6, 7]` partial → recurse.
    - `[6]` inside → 2. ✓
    - `[7]` outside → skip.

Combine: max(4, 9, 2) = 9. Visited ~O(log n) nodes.

**Intuition**: every level uses at most a couple of fully-contained nodes — the rest are either fully inside (done) or fully outside (skip).

### How an update works

To update index 3 to value 10:

- Change the leaf at index 3.
- Walk up to its parent, recomputing each ancestor's max from its two children.

Leaf has ~log n ancestors → update is O(log n).

### Storage layout

The tree is stored as a flat array. For node `i`:

- left child = `2 * i`
- right child = `2 * i + 1`
- root lives at index `1` (index `0` is unused)

Allocate `4 * n` slots — safe upper bound for any tree shape over `n` leaves.

### Two arrays, not one — important distinction

Keep these separate in your head:

**The conceptual array** (the thing the segment tree wraps around):

```
gap[0], gap[1], ..., gap[MAX_X - 1]
```

Indexed by **position on the number line**.

**The tree storage array `S`**:

```
S[1], S[2], S[3], ...
```

Indexed by **tree node id**. `S[i]` doesn't correspond to a single position — it corresponds to a **range** of positions, and stores the max of `gap` over that range:

- **Leaves** cover a single position: `S[leaf] = gap[p]` for some `p`.
- **Internal nodes** cover wider ranges and store the max of their subtree.

### Example: small picture for the obstacle problem

Suppose `MAX_X = 8` and obstacles are at positions 2 and 5. The conceptual array is:

```
position:  0   1   2   3   4   5   6   7
gap:       0   0   2   0   0   3   0   0
                   ↑           ↑
              (2 − 0 = 2)  (5 − 2 = 3)
```

The segment tree wraps around this `gap` array. `st.query(0, 5)` walks the tree, combines cached values from nodes whose ranges fit inside `[0, 5]`, and returns 3.

### Why "before index i" is a misleading mental model

A segment tree node represents an **arbitrary range** `[lo, hi]`, not a prefix. You get prefix queries (`query(0, x)`) as a *special case* — but the same tree can answer `query(3, 7)` or `query(5, 5)` equally well.

---

## The Type-2 Query Code, Line by Line

```python
i = obstacles.bisect_right(x) - 1
last = obstacles[i]
tail = x - last
best_inside = st.query(0, last)
return max(best_inside, tail) >= sz
```

Running example: `obstacles = [0, 2, 5, 9, 14]`, query `x = 10, sz = 4`.

```
0 ─── 2 ─────── 5 ─────────── 9 ── x=10 ── 14
└─2─┘ └───3───┘ └─────4─────┘ └1┘
gaps:  2        3              4    (tail)
```

### Line 1: `i = obstacles.bisect_right(x) - 1`

Find the index of the **largest obstacle ≤ x**.

`bisect_right(x)` returns the position where `x` would be inserted *after* any existing entries equal to `x`. Subtract 1 to get the rightmost index ≤ x.

- `bisect_right(10)` on `[0, 2, 5, 9, 14]` = 4 (insert before 14)
- `i = 4 − 1 = 3`

Why `bisect_right`, not `bisect_left`? If `x` equals an obstacle position (say `x = 9`), we want to *include* that obstacle. `bisect_right(9)` = 4 → `i = 3` → `obstacles[3] = 9`. ✓
With `bisect_left(9)` we'd get 3, `i = 2`, and skip the obstacle at 9. ✗

The virtual obstacle at 0 guarantees `i ≥ 0` always.

### Line 2: `last = obstacles[i]`

Look up the **position** of that obstacle. Here `last = obstacles[3] = 9`.

### Line 3: `tail = x - last`

The stretch from `last` to `x` has **no obstacle in it** (since `last` was the rightmost ≤ x). That's a free gap of length `x − last`.

Here `tail = 10 − 9 = 1`.

This is one candidate gap — easy to miss because it isn't stored in the tree.

### Line 4: `best_inside = st.query(0, last)`

Ask the segment tree: **"what's the largest gap value among positions 0 through `last`?"**

Stored gaps:

- `gap[2] = 2`
- `gap[5] = 3`
- `gap[9] = 4`
- `gap[14] = 5` ← **past `last = 9`**, correctly excluded

`st.query(0, 9)` returns `max(2, 3, 4) = 4`. The gap of 5 ending at 14 is excluded because it would extend past `x = 10` — not a legal place for the block.

**Why stop at `last` instead of `x`?** If we queried `st.query(0, x)`, we might catch a `gap[p]` where `p > x`. Such a gap *ends past x*, meaning it straddles `x`, so we can't actually use it. Stopping at `last` ensures every gap considered lies entirely within `[0, x]`.

### Line 5: `return max(best_inside, tail) >= sz`

Two candidates for the biggest usable gap in `[0, x]`:

1. `best_inside` — the best obstacle-to-obstacle gap inside `[0, last]`
2. `tail` — the leftover stretch from `last` to `x`

These together cover **every** possible spot the block could go. Take the bigger and check.

Here: `max(4, 1) = 4 ≥ 4` → **True**. (The block of size 4 fits between positions 5 and 9.)

### Two more example traces

Same obstacles, `x = 10, sz = 5`:

- `last = 9`, `tail = 1`, `best_inside = 4`.
- `max(4, 1) = 4 ≥ 5`? **False** ✓

Same obstacles, `x = 14, sz = 5`:

- `bisect_right(14) = 5`, `i = 4`, `last = 14`, `tail = 0`.
- `best_inside = st.query(0, 14) = 5` (now `gap[14] = 5` is in range).
- `max(5, 0) = 5 ≥ 5`? **True** ✓

The gap of 5 was invisible when `x = 10` because it ended past `x`. Now that `x = 14`, it's fair game. The `query(0, last)` trick handles this automatically.

---

## Complexity

- Each operation: `O(log MAX_X)` for the segment tree + `O(log n)` for `SortedList`.
- Overall: **`O((n + q) · log)`** — fast enough for `q = 1.5 · 10⁵`.

## Notes

- **Sizing the tree**: `SegmentTree(n)` covers positions `0..n-1`. `n` must be **strictly larger** than the max possible obstacle position. For this problem, `MAX_X = 50_001` is safe (constraint says `x ≤ 3 · 10⁴`).
- **Identity for max = 0**: works because gap values are always ≥ 0. For problems with negative values, use `-inf` as the "no overlap" return.
- **Recursive Python segment trees** are a bit slow but should comfortably pass within LeetCode's Python time limit for this problem. Switch to an iterative version only if you hit TLE.
- **Mental model**: think of a segment tree as a *tournament bracket*. Leaves are players (array values), each internal node is the winner (max) of its subtree. A range query asks "who would win a tournament among players in this range?" — answered by combining the precomputed winners of fully-contained sub-brackets.

See [solution.py](solution.py) for the complete working code.
