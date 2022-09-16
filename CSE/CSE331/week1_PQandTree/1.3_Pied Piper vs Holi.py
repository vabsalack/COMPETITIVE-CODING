from queue import PriorityQueue as pq


def main(arr, n, a, b, x, y, z):
    con = int()
    max_heap = pq()
    for ele in arr:
        max_heap.put(-ele)

    day_a, day_b = (z - a) // x, (z - b) // y

    while day_a >= day_b and not max_heap.empty():

        con += 1
        contri = -max_heap.get()
        a += contri
        day_a = (z - a) // x
        contri //= 2

        if contri:
            max_heap.put(-contri)

    return "RIP" if day_a > day_b else con


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, a, b, x, y, z = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        re = main(arr, n, a, b, x, y, z)
        print(re)