import sys


class Stack:
    def __init__(self, size):
        self.arr = []
        self.top = -1
        self.capacity = size

    def isFull(self):
        return True if self.top == self.capacity - 1 else False

    def isEmpty(self):
        return True if self.top == -1 else False

    def push(self, x):
        if self.isFull():
            print("OverFlow\nProgram Terminated\n")
            sys.exit(1)

        print("Inserting " + str(x))
        if len(self.arr) - 1 == self.top:
            self.top += 1
            self.arr.append(x)
        else:
            self.top += 1
            self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            print("STACK EMPTY")
            sys.exit(1)
        temp = self.top
        self.top -= 1
        print(self.arr[temp])

    def size(self):
        return self.top + 1

    def peek(self):
        return self.arr[self.top]

    def printStack(self):
        for i in range(self.top+1):
            print(self.arr[i], end=" ")
        print()
