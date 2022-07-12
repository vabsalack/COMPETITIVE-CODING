import Queue


def main():
    cq = Queue.CircularQueue(6)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    cq.printCQueue()

    cq.dequeue()
    cq.dequeue()

    cq.printCQueue()

    cq.peek()

    cq.printCQueue()


if __name__ == "__main__":
    main()