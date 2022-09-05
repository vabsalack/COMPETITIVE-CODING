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


def inorder_2(root):
    current = root
    stack = []

    while True:
        if current is not None:
            stack.append(current.left)
        elif stack:
            current = stack.pop()
            print(current.val, end="->")
            current = current.right
        else:
            break


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

    print(" \n \nIn Oder Traversal")
    Inorder(one)
    print()
    inorder_2(one)
