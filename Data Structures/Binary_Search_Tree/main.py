from BST import *


def main(array, total):
    root = None
    for x in range(total):
        root = insertNode(root, array[x])

    inorder_trav(root)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    main(arr, n)