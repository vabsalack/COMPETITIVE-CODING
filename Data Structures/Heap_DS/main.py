from HeapDS import Heap


def main():
    heap = Heap()

    heap.insert(4)
    heap.display()

    heap.insert(5)
    heap.display()

    heap.insert(6)
    heap.display()

    heap.insert(7)
    heap.display()

    heap.insert(4)
    heap.display()

    heap.insert(8)
    heap.display()

    heap.insert(14)
    heap.display()

    heap.delete(14)
    heap.display()


if __name__ == "__main__":
    main()