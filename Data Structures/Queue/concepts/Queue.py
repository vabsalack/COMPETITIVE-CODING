class CircularQueue:
    def __init__(self, size):
        self.capacity = size
        self.queue = [None]*size
        self.head = self.tail = -1

    def enqueue(self, x):
        if (self.tail + 1) % self.capacity == self.head:
            print("The circular queue is full\n")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = x
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = x

    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty\n")
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            print(temp)
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.capacity
            print(temp)

    def printCQueue(self):
        if self.head == -1:
            print("No element in the circular queue")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

    def peek(self):
        if self.head == -1:
            print("No element in the Circular queue")
            return
        print(self.queue[self.head])

