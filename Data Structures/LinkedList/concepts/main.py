from Implement_LL_python import *


def main():

    linkedlist = LinkedList()

    linkedlist.insertAtBeginning(5)
    linkedlist.insertAtBeginning(8)
    linkedlist.insertAtBeginning(7)
    linkedlist.insertAtBeginning(6)
    linkedlist.insertAtBeginning(4)
    linkedlist.insertAtBeginning(2)

    linkedlist.sortLinkedList(linkedlist.peek_head())

    linkedlist.printList()


if __name__ == "__main__":
    main()