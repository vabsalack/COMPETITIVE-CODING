from BST import *


def main():

    root = insertNode(None, 8)
    root = insertNode(root, 3)
    root = insertNode(root, 1)
    root = insertNode(root, 6)
    root = insertNode(root, 7)
    root = insertNode(root, 10)
    root = insertNode(root, 14)
    root = insertNode(root, 4)

    inorder_trav(root)
    root = insertNode(root, 0)
    print()
    inorder_trav(root)

    deleteNode(root, 7)
    print()

    inorder_trav(root)


if __name__ == "__main__":
    main()