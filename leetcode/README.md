# LeetCode Solutions

![Problems Solved](https://img.shields.io/badge/solved-66-blue)

## Statistics

| Difficulty | Count |
|------------|-------|
| Easy       | 18     |
| Medium     | 41     |
| Hard       | 7     |
| **Total**  | **66** |

## Browse by Category

- [arrays](categories/arrays.md)
- [backtracking](categories/backtracking.md)
- [dynamic-programming](categories/dynamic-programming.md)
- [graphs](categories/graphs.md)
- [greedy](categories/greedy.md)
- [hash-tables](categories/hash-tables.md)
- [heaps](categories/heaps.md)
- [linked-lists](categories/linked-lists.md)
- [math](categories/math.md)
- [searching](categories/searching.md)
- [strings](categories/strings.md)
- [trees](categories/trees.md)

[View All](categories/)

## Quick Actions

### Add New Problem

```bash
python scripts/new_problem.py <id> "<title>" [difficulty] [categories]
```

| Arg          | Required | Default  | Notes                                                 |
| ------------ | -------- | -------- | ----------------------------------------------------- |
| `id`         | yes      | —        | LeetCode problem number                               |
| `title`      | yes      | —        | Quote it; used to build the slug                      |
| `difficulty` | no       | `Medium` | `Easy`, `Medium`, or `Hard`                           |
| `categories` | no       | `arrays` | Comma-separated, quoted (e.g. `"arrays,hash-tables"`) |

Category names are normalized to kebab-case and pluralized when needed (`Hash Table` → `hash-tables`, `array` → `arrays`). Words in the special list (`dynamic-programming`, `searching`, `sorting`, `backtracking`, `greedy`, `math`) are left as-is.

Examples:
```bash
python scripts/new_problem.py 1 "Two Sum" Easy "arrays,hash-tables"
python scripts/new_problem.py 42 "Trapping Rain Water" Hard "arrays,dynamic-programming"
python scripts/new_problem.py 100 "Same Tree" Easy "trees"
```

### Regenerate Indexes

LeetCode-only views (this README + `categories/*.md`):
```bash
python scripts/generate_indexes.py
```

Cross-platform topic pages (`topics/*/problems.md`), run from repo root:
```bash
python scripts/generate_topic_problems.py
```

To change a problem's categories after creation, edit its entry in [metadata.json](metadata.json) and re-run both scripts.

## All Problems

| # | Title | Difficulty | Categories |
|---|-------|------------|------------|
| 1 | [Two Sum](problems/0001-two-sum) | Easy | arrays, hash-tables |
| 19 | [Remove Nth Node From End of List](problems/0019-remove-nth-node-from-end-of-list) | Medium | linked-lists |
| 22 | [Generate Parentheses](problems/0022-generate-parentheses) | Medium | backtracking |
| 35 | [Search Insert Position](problems/0035-search-insert-position) | Easy | searching |
| 39 | [Combination Sum](problems/0039-combination-sum) | Medium | backtracking |
| 40 | [Combination Sum II](problems/0040-combination-sum-ii) | Medium | backtracking |
| 46 | [Permutations](problems/0046-permutations) | Medium | backtracking |
| 47 | [Permutations II](problems/0047-permutations-ii) | Medium | backtracking |
| 48 | [Rotate image](problems/0048-rotate-image) | Medium | arrays |
| 51 | [N-Queens](problems/0051-n-queens) | Hard | backtracking |
| 61 | [Rotate list](problems/0061-rotate-list) | Medium | linked-lists |
| 70 | [Climbing Stairs](problems/0070-climbing-stairs) | Easy | dynamic-programming |
| 78 | [Subsets](problems/0078-subsets) | Medium | backtracking |
| 83 | [Remove Duplicates from Sorted List](problems/0083-remove-duplicates-from-sorted-list) | Easy | linked-lists |
| 93 | [Restore IP Addresses](problems/0093-restore-ip-addresses) | Medium | backtracking |
| 153 | [Find Minimum in Rotated Sorted Array](problems/0153-find-minimum-in-rotated-sorted-array) | Medium | arrays, searching |
| 154 | [Find Minimum in Rotated Sorted Array II](problems/0154-find-minimum-in-rotated-sorted-array-ii) | Hard | arrays, searching |
| 203 | [Remove Linked List Elements](problems/0203-remove-linked-list-elements) | Easy | linked-lists |
| 215 | [Kth Largest Element in an Array](problems/0215-kth-largest-element-in-an-array) | Medium | heaps |
| 216 | [Combination Sum III](problems/0216-combination-sum-iii) | Medium | backtracking |
| 234 | [Palindrome Linked List](problems/0234-palindrome-linked-list) | Easy | linked-lists |
| 309 | [Best Time to Buy and Sell Stock with Cooldown](problems/0309-best-time-to-buy-and-sell-stock-with-cooldown) | Medium | dynamic-programming |
| 322 | [Coin Change](problems/0322-coin-change) | Medium | dynamic-programming |
| 328 | [Odd Even Linked List](problems/0328-odd-even-linked-list) | Medium | linked-lists |
| 396 | [Rotate Function](problems/0396-rotate-function) | Medium | arrays, dynamic-programming |
| 560 | [Subarray Sum Equals K](problems/0560-subarray-sum-equals-k) | Medium | arrays, hash-tables |
| 703 | [Kth Largest Element in a Stream](problems/0703-kth-largest-element-in-a-stream) | Easy | heaps |
| 707 | [Design Linked List](problems/0707-design-linked-list) | Medium | linked-lists |
| 788 | [Rotated Digits](problems/0788-rotated-digits) | Medium | math |
| 796 | [Rotate string](problems/0796-rotate-string) | Easy | strings |
| 797 | [All Paths From Source to Target](problems/0797-all-paths-from-source-to-target) | Medium | backtracking, graphs |
| 967 | [Numbers With Same Consecutive Differences](problems/0967-numbers-with-same-consecutive-differences) | Medium | backtracking |
| 973 | [K Closest Points to Origin](problems/0973-k-closest-points-to-origin) | Medium | heaps |
| 1167 | [Minimum Cost to Connect Sticks](problems/1167-minimum-cost-to-connect-sticks) | Medium | heaps |
| 1196 | [How Many Apples Can You Put into the Basket](problems/1196-how-many-apples-can-you-put-into-the-basket) | Easy | greedy |
| 1231 | [Divide Chocolate](problems/1231-divide-chocolate) | Hard | searching |
| 1283 | [Find the Smallest Divisor Given a Threshold](problems/1283-find-the-smallest-divisor-given-a-threshold) | Medium | searching |
| 1290 | [Convert Binary Number in a Linked List to Integer](problems/1290-convert-binary-number-in-a-linked-list-to-integer) | Easy | linked-lists |
| 1323 | [Maximum 69 Number](problems/1323-maximum-69-number) | Easy | greedy |
| 1338 | [Reduce Array Size to The Half](problems/1338-reduce-array-size-to-the-half) | Medium | greedy |
| 1344 | [Angle Between Hands of a Clock](problems/1344-angle-between-hands-of-a-clock) | Medium | math |
| 1426 | [Counting Elements](problems/1426-counting-elements) | Easy | hash-tables |
| 1665 | [Minimum Initial Energy to Finish Tasks](problems/1665-minimum-initial-energy-to-finish-tasks) | Hard | arrays, greedy |
| 1710 | [Maximum Units on a Truck](problems/1710-maximum-units-on-a-truck) | Easy | greedy |
| 1721 | [Swapping Nodes in a Linked List](problems/1721-swapping-nodes-in-a-linked-list) | Medium | linked-lists |
| 1732 | [Find the Highest Altitude](problems/1732-find-the-highest-altitude) | Easy | arrays |
| 1832 | [Check if the Sentence Is Pangram](problems/1832-check-if-the-sentence-is-pangram) | Easy | hash-tables, strings |
| 1861 | [Rotating the Box](problems/1861-rotating-the-box) | Medium | arrays |
| 1962 | [Remove Stones to Minimize the Total](problems/1962-remove-stones-to-minimize-the-total) | Medium | heaps |
| 2033 | [Minimum Operations to Make a Uni-Value Grid](problems/2033-minimum-operations-to-make-a-uni-value-grid) | Medium | arrays |
| 2074 | [Reverse Nodes in Even Length Groups](problems/2074-reverse-nodes-in-even-length-groups) | Medium | linked-lists |
| 2095 | [Delete the Middle Node of a Linked List](problems/2095-delete-the-middle-node-of-a-linked-list) | Medium | linked-lists |
| 2130 | [Maximum Twin Sum of a Linked List](problems/2130-maximum-twin-sum-of-a-linked-list) | Medium | linked-lists |
| 2196 | [Create Binary Tree From Descriptions](problems/2196-create-binary-tree-from-descriptions) | Medium | trees, hash-tables |
| 2389 | [Longest Subsequence With Limited Sum](problems/2389-longest-subsequence-with-limited-sum) | Easy | searching |
| 2784 | [Check if Array is Good](problems/2784-check-if-array-is-good) | Easy | arrays, hash-tables |
| 3612 | [Process String with Special Operations I](problems/3612-process-string-with-special-operations-i) | Medium | strings |
| 3614 | [Process String with Special Operations II](problems/3614-process-string-with-special-operations-ii) | Hard | strings |
| 3633 | [Earliest Finish Time for Land and Water Rides I](problems/3633-earliest-finish-time-for-land-and-water-rides-i) | Medium | arrays |
| 3635 | [Earliest Finish Time for Land and Water Rides II](problems/3635-earliest-finish-time-for-land-and-water-rides-ii) | Medium | arrays |
| 3660 | [Jump Game IX](problems/3660-jump-game-ix) | Medium | arrays |
| 3691 | [Maximum Total Subarray Value II](problems/3691-maximum-total-subarray-value-ii) | Hard | heaps, greedy |
| 3742 | [Maximum Path Score in a Grid](problems/3742-maximum-path-score-in-a-grid) | Medium | dynamic-programming |
| 3751 | [Total Waviness of Numbers in Range I](problems/3751-total-waviness-of-numbers-in-range-i) | Medium | arrays |
| 3753 | [Total Waviness of Numbers in Range II](problems/3753-total-waviness-of-numbers-in-range-ii) | Hard | dynamic-programming |
| 3838 | [Weighted Word Mapping](problems/3838-weighted-word-mapping) | Easy | strings |

---

*Last updated: 2026-06-19*
