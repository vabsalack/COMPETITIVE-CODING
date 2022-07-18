from Circular_Queue import CircularQueue


def main():
    queue = CircularQueue(10)
    for i in range(10):
        queue.push_element(i)

    queue.print_queue()

    for _ in range(5):
        queue.pop_element()

    queue.print_queue()

    queue.push_element(10)
    queue.push_element(11)

    queue.print_queue()


if __name__ == "__main__":
    main()