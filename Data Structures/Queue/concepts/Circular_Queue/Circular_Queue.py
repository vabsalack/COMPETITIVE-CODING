
class CircularQueue:
    def __init__(self, size):
        self.capacity = size
        self.arr = [None]*size
        self.front = -1
        self.rear = -1

    def is_full(self):
        if (self.front == 0 and self.rear == self.capacity - 1) or (self.front == self.rear + 1):
            return True
        return False

    def is_empty(self):
        return self.front == -1

    def push_element(self, element):

        if self.is_full():
            print("Queue OverFlow...")
            return

        if self.front == -1 and self.rear == -1:
            self.rear = 0
            self.front = 0
            self.arr[self.rear] = element
            return

        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = element

    def pop_element(self):

        if self.is_empty():
            print("Queue UnderFlow...")
            return

        temp = self.arr[self.front]

        if self.front == self.rear:
            self.rear = -1
            self.front = -1
            print(temp)
            return

        self.front = (self.front + 1) % self.capacity
        print(temp)
        return

    def print_queue(self):

        if self.is_empty():
            print("Circular Queue is empty")
            return
        if self.rear >= self.front:
            for index in range(self.front, self.rear + 1):
                print(self.arr[index], end=" ")
            print()
            return
        else:
            for index in range(self.front, self.capacity):
                print(self.arr[index], end=" ")
            for index in range(0, self.rear+1):
                print(self.arr[index], end=" ")
            print()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print(self.arr[self.front])





