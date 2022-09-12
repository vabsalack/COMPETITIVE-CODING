memo = [-1] * 1000
memo[0] = 0


def Tiling(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = Tiling(n - 1) + Tiling(n - 2)
    return memo[n]


if __name__ == "__main__":
    print(Tiling(int(input())))
