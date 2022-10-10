from collections import Counter
import sys

sys.setrecursionlimit(10000)


def main(arr, n, k):
    a = [0] * n
    i = 0
    used = Counter(arr)
    for x in arr:
        if used[x] == 0:
            continue
        a[i] = x - (k - 1) * a[0] if i != 0 else x // k

        def set_used(summ, idx, cnt):

            if cnt == k:
                used.subtract([summ])
                return

            set_used(summ + a[idx], idx, cnt + 1)

            if idx > 0:
                set_used(summ, idx - 1, cnt)

        set_used(a[i], i, 1)

        i += 1
        if i == n:
            break
    return a


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        S = list(sorted(map(int, input().split())))
        re = main(S, n, k)
        print(*re)