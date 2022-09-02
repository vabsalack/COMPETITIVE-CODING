def sieve_count(x):
    sieve1 = [1]*(x+1)
    sieve1[0] = sieve1[1] = 0
    for i in range(2, x+1):
        if sieve1[i] == 1:
            for j in range(i*i, x+1, i):
                sieve1[j] = 0
    s = 0
    sie_count1 = [0]*(x+1)
    for i in range(x+1):
        s += sieve1[i]
        sie_count1[i] = s
    return sieve1, sie_count1


sieve, sie_count = sieve_count(1000000)


def main(l, r):
    count = 0
    for i in range(l, r + 1):
        if sieve[sie_count[i]]:
            count += 1
    return count


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        re = main(l, r)
        print(re)