from Priority_Queue import PriorityQueue


def main():
    pq = PriorityQueue()
    pq.insertNode(0)
    pq.insertNode(5)
    pq.insertNode(6)
    pq.insertNode(8)
    pq.peek()
    pq.print_queue()


if __name__ == "__main__":
    main()