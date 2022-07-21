class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    #  Inserting at the beginning
    def peek_head(self):
        return self.head

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    #  Insert after a Node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must LinkedList")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):
        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # find key to  be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # if the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    # search an element
    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                #  index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    def printList(self):
        temp = self.head
        while temp:
            print(f"{temp.data}-->", end="")
            temp = temp.next
        print("None")






