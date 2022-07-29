class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def Inorder(root):
    """ traverse left-root-right"""
    if root:
        # traverse left
        Inorder(root.left)
        # traverse root
        print(str(root.val) + "->", end="")
        # traverse right
        Inorder(root.right)


def Postorder(root):
    """ traverse left-right-root"""
    if root:
        # traverse left
        Postorder(root.left)
        # traverse right
        Postorder(root.right)
        # traverse root
        print(str(root.val) + "->", end="")


def Preorder(root):
    """ traverse root-left-right"""
    if root:
        "traverse root"
        print(str(root.val) + "->", end="")
        "traverse left"
        Preorder(root.left)
        "traverse right"
        Preorder(root.right)


if __name__ == "__main__":

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    four.left = six
    four.right = seven

    five.left = eight

    three.left = nine
    three.right = ten

    nine.left = eleven
    ten.left = twelve

    print("Pre Oder Traversal ")
    Preorder(one)
    print(" \n \nIn Oder Traversal")
    Inorder(one)
    print("\n \n Post Oder Traversal")
    Postorder(one)

