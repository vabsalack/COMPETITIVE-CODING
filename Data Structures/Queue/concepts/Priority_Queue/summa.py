class pq:
    def __init__(self):
        self.arr = []

    def heapifY(self, n, i):
        largest = i
        left = 2 * largest + 1
        right = 2 * largest + 2

        if left < n and self.arr[largest] < self.arr[left]:
            largest = left
        if right < n and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapifY(n, largest)

    def insertnode(self, element):
        size = len(self.arr)
        self.arr.append(element)
        if size == 1:
            return
        else:
            size = len(self.arr)
            for i in range(size // 2 - 1, -1, -1):
                self.heapifY(size, i)

    def deletenode(self, element):
        size = len(self.arr)
        i = 0
        for i in range(0, size):
            if element == self.arr[i]:
                break

        self.arr[i], self.arr[size - 1] = self.arr[size - 1], self.arr[i]

        self.arr.remove(size - 1)

        for i in range((len(self.arr) // 2) - 1, -1, -1):
            self.heapifY(len(self.arr), i)

    def peek(self):
        return self.arr[0]


def main(A, N, Z):
    ar = pq()
    for ele in A:
        ar.insertnode(ele)
    attack = 0
    while Z != 0 or not any(ar.arr):
        temp = ar.peek()
        Z -= temp
        attack += 1
        ar.arr[0] = temp // 2
        ar.heapifY(N, N // 2 - 1)
    return attack


if __name__ == "__main__":

    t = int(input())
    for _ in range(t):

        N, Z = list(map(int, input().split()))
        A = list(map(int, input().split()))
        re = main(A, N, Z)
        print(re)