class Solution:
    """https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/"""
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next