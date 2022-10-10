def fib(n):
    """0, 1
       1 1 2 3 5 8 13 21 ..."""
    if n in memo:
        return memo[n]

    if n < 2:
        return 1

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


if __name__ == "__main__":
    memo = {}
    print(fib(int(input())))
    print(memo)



