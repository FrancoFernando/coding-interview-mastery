# Greedy

## Overview

Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum. They work when the problem has optimal substructure and the greedy choice property.

## Key Concepts

- **Greedy Choice Property**: A globally optimal solution can be reached by making locally optimal choices
- **Optimal Substructure**: An optimal solution contains optimal solutions to subproblems
- **No Backtracking**: Once a choice is made, it's never reconsidered

## Common Patterns

1. **Activity Selection** - Select maximum non-overlapping activities
2. **Fractional Knapsack** - Maximize value with weight constraint
3. **Huffman Coding** - Optimal prefix-free encoding
4. **Interval Scheduling** - Schedule maximum intervals
5. **Minimum Spanning Tree** - Kruskal's and Prim's algorithms

## When to Use Greedy

- Problem asks for maximum/minimum of something
- Sorting often helps reveal the greedy strategy
- Making the best choice now doesn't hurt future choices
- Local optimum leads to global optimum

## Greedy vs Dynamic Programming

| Greedy | Dynamic Programming |
|--------|---------------------|
| Makes one choice per step | Considers all choices |
| No backtracking | May revisit decisions |
| Faster (usually O(n log n)) | Slower (usually O(n²) or more) |
| Doesn't always work | Always finds optimal if applicable |

## Common Approach

1. Sort the input (often by some criterion)
2. Iterate and make the locally optimal choice
3. Update state and continue

## Tips

1. **Prove correctness** - Greedy doesn't always work; verify the greedy choice is safe
2. **Sort first** - Many greedy problems require sorting
3. **Consider edge cases** - Empty input, single element, all same values
4. **Compare with DP** - If greedy fails, try dynamic programming

## Notes

[Add your study notes here]
