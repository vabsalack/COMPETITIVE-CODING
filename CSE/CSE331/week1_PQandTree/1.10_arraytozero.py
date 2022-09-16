from queue import PriorityQueue


def main(arr, n):

    q = PriorityQueue()

    for ele in arr:
        q.put(-ele)
    count = 0

    while q.qsize() >= 2:

        element1 = -1*q.get()
        element2 = -1*q.get()

        element1 -= 1
        element2 -= 1

        count += 2

        if element1 > 0:
            q.put(-element1)
        if element2 > 0:
            q.put(-element2)

    return count if q.qsize() == 0 else -1


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    re = main(arr, n)
    print(re)