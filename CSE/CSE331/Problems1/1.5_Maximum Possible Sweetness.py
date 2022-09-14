
import heapq


def main(d, prices, sweet):
    listt = list(zip(sweet, prices))
    heapq._heapify_max(listt)
    sweetness = int()

    while d > 0 and len(listt) != 0:

        s, p = heapq._heappop_max(listt)
        print(s, p)
        heapq._heapify_max(listt)

        if p <= d:
            d -= p
            sweetness += s

    return sweetness


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, d = list(map(int, input().split()))
        prices = list(map(int, input().split()))
        sweet = list(map(int, input().split()))
        re = main(d, prices, sweet)
        print(re)