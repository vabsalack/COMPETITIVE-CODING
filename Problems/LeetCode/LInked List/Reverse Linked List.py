class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/"""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        head = previous
        return head