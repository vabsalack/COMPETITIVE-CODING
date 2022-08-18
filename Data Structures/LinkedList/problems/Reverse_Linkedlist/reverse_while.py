class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse(head):
    current = head
    previous = None
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    head = previous
    return head


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    cur = a
    while cur is not None:
        print(cur.value, end="-->")
        cur = cur.next

    print()

    r = reverse(a)
    cur = r
    while cur is not None:
        print(cur.value, end="-->")
        cur = cur.next
