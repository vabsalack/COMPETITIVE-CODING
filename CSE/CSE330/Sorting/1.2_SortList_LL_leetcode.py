# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # find midpoint
        midnode = self.midpoint(head)

        # left/right recursive
        left = self.sortList(head)
        right = self.sortList(midnode)

        # merge
        return self.merge(left, right)

    def midpoint(self, head):

        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        return mid

    def merge(self, left, right):
        dummy = cur = ListNode(0)
        while left and right:
            cur.next = left if left.val < right.val else right
            if cur.next is left:
                left = left.next
            else:
                right = right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next
