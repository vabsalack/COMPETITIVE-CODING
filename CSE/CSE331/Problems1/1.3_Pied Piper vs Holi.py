# cook your dish here
import heapq as q


def decide(a, b, x, y, z):
    t1 = (z - a) / x
    t2 = (z - b) / y
    return t1 >= t2


def main(ar1, c):
    ans = int()
    q._heapify_max(c)
    a, b, x, y, z = ar1[1:]
    while c[0] != 0 and decide(a, b, x, y, z):
        ans += 1
        temp = q._heappop_max(c)
        a += temp
        q.heappush(c, temp // 2)
        q._heapify_max(c)

    if decide(a, b, x, y, z):
        print("RIP")
    else:
        print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        ar1 = list(map(int, input().split()))
        c = list(map(int, input().split()))
        main(ar1, c)