import heapq


def main(arr, n):
    total = sum(arr)
    ans = {0: total}

    min_heap = arr[::]
    max_heap = [-x for x in arr]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    for i in range(1, n):
        max_value = -heapq.heappop(max_heap)
        min_value = heapq.heappop(min_heap)
        heapq.heappush(min_heap, max_value - min_value)
        heapq.heappush(max_heap, min_value - max_value)
        ans[i] = ans[i - 1] - 2 * min_value

    return ans


if __name__ == "__main__":
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = main(arr, n)
    for _ in range(q):
        k = int(input())
        print(ans[k])
