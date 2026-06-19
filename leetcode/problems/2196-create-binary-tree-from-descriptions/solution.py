"""
LeetCode #2196: Create Binary Tree From Descriptions
Difficulty: Medium
Link: https://leetcode.com/problems/create-binary-tree-from-descriptions/
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set([d[1] for d in descriptions])
        parents = set([d[0] for d in descriptions])
        all_values = children | parents
        nodes = {val: TreeNode(val) for val in all_values}
        root = next(iter(all_values ^ children))
        for p, c, is_left in descriptions:
            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
        return nodes[root]


def _inorder(node):
    if node is None:
        return []
    return _inorder(node.left) + [node.val] + _inorder(node.right)


def test_solution():
    sol = Solution()

    root = sol.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
    assert root.val == 50
    assert _inorder(root) == [15, 20, 17, 50, 19, 80]
    print("Test 1 passed")

    root = sol.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]])
    assert root.val == 1
    assert _inorder(root) == [2, 4, 3, 1]
    print("Test 2 passed")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
