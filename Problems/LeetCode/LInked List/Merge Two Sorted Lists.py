# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/"""

    def insert_node(self, node, list2):
        head = list2

        if node.val <= head.val:
            node.next = head
            return node

        current = head

        while current.next is not None:

            if current.val <= node.val <= current.next.val:
                node.next = current.next
                current.next = node
                return head

            current = current.next

        current.next = node
        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr = list1

        while curr is not None:
            temp = ListNode(curr.val)
            list2 = self.insert_node(temp, list2)
            curr = curr.next

        return list2