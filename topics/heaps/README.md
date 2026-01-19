# Heaps

## Overview

A heap is a specialized tree-based data structure that satisfies the heap property. In a max heap, parent nodes are always greater than or equal to children. In a min heap, parent nodes are always less than or equal to children.

## Key Concepts

- **Min Heap**: Root is the minimum element
- **Max Heap**: Root is the maximum element
- **Complete Binary Tree**: All levels filled except possibly the last
- **Heap Property**: Parent-child ordering relationship
- **Priority Queue**: Abstract data type often implemented with heaps

## Common Patterns

1. **Top K Elements** - Find k largest/smallest elements
2. **K-th Element** - Find the k-th largest/smallest
3. **Merge K Sorted** - Merge k sorted lists/arrays
4. **Stream Processing** - Maintain order in streaming data
5. **Scheduling** - Process items by priority

## Time Complexities

| Operation | Time |
|-----------|------|
| Insert | O(log n) |
| Extract Min/Max | O(log n) |
| Peek Min/Max | O(1) |
| Build Heap | O(n) |
| Heapify | O(log n) |

## Python heapq Module

```python
import heapq

# Min heap operations
heap = []
heapq.heappush(heap, item)      # Insert
min_item = heapq.heappop(heap)  # Extract min
min_item = heap[0]              # Peek min

# Build heap from list
heapq.heapify(nums)             # O(n)

# Top k smallest/largest
heapq.nsmallest(k, nums)
heapq.nlargest(k, nums)

# Max heap trick: negate values
heapq.heappush(heap, -item)
max_item = -heapq.heappop(heap)
```

## Tips

1. Python's heapq is a **min heap** by default
2. For max heap, negate values when pushing/popping
3. Use tuples for custom priority: `(priority, item)`
4. For k largest, use min heap of size k
5. For k smallest, use max heap of size k

## Notes

[Add your study notes here]
