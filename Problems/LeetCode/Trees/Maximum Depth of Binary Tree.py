# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        """ compare the depth of sub left and right tree and return result + 1
            break to sub problems to find depth of left and right subtree."""

        # base case
        if root is None:
            return 0

        # main logic
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)

        return ld + 1 if ld > rd else rd + 1



