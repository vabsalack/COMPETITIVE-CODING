# cook your dish here
from heapq import heappush as push, heappop as pop


def pre_compute(k, mov, sat):
    result = []
    arr = []
    mov.sort()
    sat.sort()
    for i in range(k):
        end = min(k, 10001 // (i + 1))
        for j in range(end):
            push(arr, (mov[i] + sat[j]))

    c = 10000

    while bool(arr) and c != 0:
        result.append(pop(arr))
        c -= 1

    return result


if __name__ == "__main__":

    t = int(input())
    for _ in range(t):
        k, q = list(map(int, input().split()))
        mov = list(map(int, input().split()))
        sat = list(map(int, input().split()))
        arr = pre_compute(k, mov, sat)
        for _ in range(q):
            ith = int(input())
            print(arr[ith - 1])