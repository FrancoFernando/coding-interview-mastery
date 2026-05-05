"""
LeetCode #61: Rotate list
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-list/
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        fast = slow = head
        rotations = self.remainingRotations(head, k)

        if rotations == 0:
            return head

        for _ in range(rotations):
            fast = fast.next

        while fast is not None and  fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head

    def remainingRotations(self, head, k):
        length = 0
        while head is not None:
            head = head.next
            length += 1
        return 0 if length == 0 else k % length

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
