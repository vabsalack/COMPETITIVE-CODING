class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):

        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    # Write your code here
    heights = dict()

    def recursion(root, h, l):

        if root is not None:
            temp = (root, l)

            if h not in heights:
                heights[h] = temp
            elif heights[h][1] > l:
                heights[h] = temp

            recursion(root.left, h - 1, l + 1)
            recursion(root.right, h + 1, l + 1)

    recursion(root, 0, 0)

    for key in sorted(heights):
        print(heights[key][0].info, end=" ")



