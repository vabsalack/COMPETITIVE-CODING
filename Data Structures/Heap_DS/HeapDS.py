class Heap:
    def __init__(self):
        self.arr = list()

    def heapify(self, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n and self.arr[i] < self.arr[l]:
            largest = l

        if r < n and self.arr[largest] < self.arr[r]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def insert(self, new_num):
        size = len(self.arr)
        if not size:
            self.arr.append(new_num)
        else:
            self.arr.append(new_num)
            size = len(self.arr)
            for i in range((size//2 - 1), -1, -1):
                self.heapify(size, i)

    def delete(self, num):
        size = len(self.arr)
        i = 0
        for i in range(0, size):
            if self.arr[i] == num:
                break

        self.arr[i], self.arr[size - 1] = self.arr[size - 1], self.arr[i]

        self.arr.remove(num)
        #  self.arr.pop()
        size = len(self.arr)
        for i in range(((size//2) - 1), -1, -1):
            self.heapify(size, i)

    def display(self):
        print(*self.arr)




