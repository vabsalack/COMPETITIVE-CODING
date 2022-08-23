class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/"""
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return head

        current = head
        i = 0
        while i < n:
            current = current.next
            i += 1

        if current is None:
            return head.next

        l, r = head, current

        while r.next is not None:
            r = r.next
            l = l.next

        l.next = l.next.next

        return head