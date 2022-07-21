class PriorityQueue:
    """Implementing Priority Queue using Max Heap Binary tree data structure"""
    def __init__(self):
        self.arr = []

    def heapify(self, n, i):

        largest = i

        left = 2 * largest + 1
        right = 2 * largest + 2

        if left < n and self.arr[i] < self.arr[left]:
            largest = left
        if right < n and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def insertNode(self, element):
        size = len(self.arr)
        if size == 0:
            self.arr.append(element)
        else:
            self.arr.append(element)
            for i in range((size//2 - 1), -1, -1):
                self.heapify(size, i)

    def deleteNode(self, element):
        size = len(self.arr)
        i = 0
        for i in range(0, size):
            if element == self.arr[i]:
                break

        self.arr[i], self.arr[size-1] = self.arr[size - 1], self.arr[i]

        self.arr.remove(size - 1)

        for i in range((len(self.arr)//2) - 1, -1, -1):
            self.heapify(len(self.arr), i)

    def peek(self):
        print(self.arr[0])

    def print_queue(self):
        print(*self.arr, sep=" ")

