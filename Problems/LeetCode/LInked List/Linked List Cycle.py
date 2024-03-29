# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/"""
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head

        while True:

            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True