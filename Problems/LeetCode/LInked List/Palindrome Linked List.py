# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/"""
    def reverse_ll(self, head):
        current = head
        previous = None
        next = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

    def comparelist(self, head1, head2):
        temp1 = head1
        temp2 = head2

        while temp1 and temp2:
            if temp1.val == temp2.val:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return False

        if temp1 is None and temp2 is None:
            return True
        return False

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        pre_slow = head

        midnode = None

        res = True

        if head is not None and head.next is not None:

            while fast is not None and fast.next is not None:
                fast = fast.next.next
                pre_slow = slow
                slow = slow.next

            if fast is not None:
                midnode = slow
                slow = slow.next

            second = slow

            pre_slow.next = None

            second = self.reverse_ll(second)

            res = self.comparelist(head, second)

        return res