class Node:
    def __init__(self, data):
        print(f"Node initialized with {data}")
        self.data = data
        self.next = None

    def __str__(self):
        return str(id(self))


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, value):
        if not self.head:
            self.head = Node(value)
            print(f"head was created..")
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = Node(value)
            print(f"Node appended")

    def print_ll(self):
        temp_node = self.head

        if temp_node is not None:
            if temp_node.next is None:
                print(f"{temp_node.data}", end="\n")
            while temp_node.next:
                print(f"[Node address: {temp_node}, data: {temp_node.data},next_add: {temp_node.next}]-->", end=" ")
                temp_node = temp_node.next
            print("None")
        else:
            print(f"Linked list is empty")


def main(n):
    ll = LinkedList()
    for _ in range(n):
        ll.insertNode(int(input("Enter Node data value> ")))
    ll.print_ll()


if __name__ == "__main__":
    t = int(input("Enter number of Nodes> "))
    main(t)
