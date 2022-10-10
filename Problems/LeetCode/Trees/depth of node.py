def find_depth(root, x):
    """initially preorder traversal, if element found we then calculate depth exclusive from that node -1, -1+1, 0+1
       ,.... when the first recursive call reached return dist"""

    # base case 1
    if root is None:
        return -1

    dist = -1

    # base case 2
    if root.data == x:
        return dist + 1

    # main logic
    find_depth(root.left, x)
    if dist > -1:
        return dist + 1

    find_depth(root.right, x)
    if dist > -1:
        return dist + 1

    return dist


def find_height(root1, x1):

    """ height of a node is same as maximum depth of that node. when we calculate the maximum depth of the tree
        (left and right subtree)
        assign global height to depth calculated when the root is the value"""

    global height
    height = -1

    def fhon(root, x):
        global height
        # base case
        if root is None:
            return 0

        # main logic
        lh = fhon(root.left, x)
        rh = fhon(root.right, x)

        if root.value == x:
            height = max(lh, rh)

        return lh + 1 if lh > rh else rh + 1

    fhon(root1, x1)
    return height






