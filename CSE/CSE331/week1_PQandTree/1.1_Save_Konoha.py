import heapq as hq


def main(a, n, z):
    attack = 0
    hq._heapify_max(a)

    while z > 0 and a[0] != 0:
        attack += 1
        temp = hq.heappop(a)
        z -= temp
        hq.heappush(a, temp // 2)
        hq._heapify_max(a)

    return "Evacuate" if z > 0 else attack


if __name__ == '__main__':
    t = input()
    n, z = list(map(int, input().split()))
    a = list(map(int, input().split()))
    re = main(a, n, z)
    print(re)