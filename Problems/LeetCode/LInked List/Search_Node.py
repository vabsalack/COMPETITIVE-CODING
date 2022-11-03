class node:
    def __init__(self, value, nex=None):
        self.data = value
        self.next = nex


def search_node(head, target, i):
    if head is None:
        return "Not found"
    if head.data == target:
        return f"Target is in {i} 1-indexing"
    return search_node(head.next, target, i+1)


if __name__ == "__main__":
    one = node(1)
    two = node(2)
    three = node(3)

    one.next = two
    two.next = three

    print(search_node(one, 3, 1))



