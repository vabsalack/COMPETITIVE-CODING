from queue import PriorityQueue as pq


def main(arr, n, z):
    att = int()
    max_heap = pq()
    for ele in arr:
        max_heap.put(-ele)

    while z > 0 and not max_heap.empty():

        att += 1
        sold = -max_heap.get()

        z -= sold
        sold //= 2

        if sold:
            max_heap.put(-sold)

    if z > 0:
        return -1

    return att


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, z = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        re = main(arr, n, z)
        print("Evacuate" if re == -1 else re)