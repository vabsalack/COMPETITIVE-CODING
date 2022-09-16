from queue import PriorityQueue as pq


def main(arr, n):
    count = 0
    max_heap = pq()

    for ele in arr:
        max_heap.put(-ele)

    while max_heap.qsize() >= 2:

        first = -max_heap.get()
        second = -max_heap.get()

        first -= 1
        second -= 1

        count += 2

        if first not in [0]:
            max_heap.put(-first)
        if second not in [0]:
            max_heap.put(-second)

    return count if max_heap.empty() else -1


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    re = main(arr, n)
    print(re)