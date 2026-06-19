# 2196. Create Binary Tree From Descriptions

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions/)

## Problem Description

You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_i, child_i, isLeft_i]` indicates that `parent_i` is the parent of `child_i` in a binary tree of unique values. Furthermore:

- If `isLeft_i == 1`, then `child_i` is the left child of `parent_i`.
- If `isLeft_i == 0`, then `child_i` is the right child of `parent_i`.

Construct the binary tree described and return its root.

The test cases will be generated such that the binary tree is valid.

## Approach

1. Collect every value appearing as a child and every value appearing as a parent.
2. Create one `TreeNode` per distinct value, stored in a dictionary keyed by value so each edge can wire two existing nodes together in O(1).
3. The root is the single value that is a parent but never a child. Since `children ⊆ all_values`, the symmetric difference `all_values ^ children` collapses to exactly that set.
4. Walk the descriptions a second time and attach each child as the left or right pointer of its parent.

## Complexity

- **Time Complexity:** O(N) where N is the number of descriptions. Set construction, dict construction, and the wiring pass are each linear.
- **Space Complexity:** O(N) for the node dictionary and auxiliary sets.

## Notes

- `next(iter(...))` avoids materializing the set as a list just to grab one element.
- Tuple unpacking in `for p, c, is_left in descriptions` reads more cleanly than indexing `d[0]/d[1]/d[2]`.
- A single-pass variant is possible: build nodes lazily inside the wiring loop and track a `has_parent` set; the two-pass form above is easier to reason about and has the same asymptotic cost.
