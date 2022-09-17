def printlevelorder(root):
    """ print level order traversal of tree using while loop and queue data structure without recursion"""
    queue = [root]

    while len(queue) > 0:

        node = queue.pop(0)

        if node is None:
            return

        print(node.info, end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

##########################################################################################################

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
        if self.root == None:
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


def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printcurrentlevel(root, level):
    level_element = []

    def pcl(root, level):

        if root is None:
            return

        if level == 1:
            level_element.append(root.info)

        elif level > 1:
            pcl(root.left, level - 1)
            pcl(root.right, level - 1)

    pcl(root, level)
    return level_element


def levelOrder(root):
    # Write your code here
    h = height(root)
    re = []
    for i in range(1, h + 1):
        re.extend(printcurrentlevel(root, i))
    print(*re)

