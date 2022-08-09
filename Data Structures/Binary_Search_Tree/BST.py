class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}"


def private_search_node(root, key):
    if root is None:
        return None
    if key == root.key:
        return root
    if key < root.key:
        return private_search_node(root.left, key)
    if key > root.key:
        return private_search_node(root.right, key)


def search_node(root, key):
    result = private_search_node(root, key)
    if result is not None:
        print(f"Node {root} found")
        return
    print(f"Node {root} not found")


def inorder_trav(root):
    if root is not None:
        #  traverse left
        inorder_trav(root.left)
        #  traverse root
        print(str(root.key) + "->", end=' ')
        #  traverse right
        inorder_trav(root.right)


def insertNode(node, key):
    if node is None:
        return Node(key)

    #  if the node key is greater the passed key, insert key to left subtree, recursive
    if key < node.key:
        node.left = insertNode(node.left, key)
    #  if the node key less the passed key, insert key to right subtree, recursive
    else:
        node.right = insertNode(node.right, key)

    #  return the newly created node to the parent node
    return node


def find_inorder_successor(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, key):
    #  return if tree is empty
    if root is None:
        return root

    #  search given key in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
    #  search given key in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        #  if the traverse node is the given node

        #  if left node is None or node has no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        #  if right node is None
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        #  if the node has two child, find the inorder successor and replace its key.
        temp = find_inorder_successor(root.right)

        root.key = temp.key

        #  delete the inorder successor node
        root.right = deleteNode(root.right, temp.key)

    return root