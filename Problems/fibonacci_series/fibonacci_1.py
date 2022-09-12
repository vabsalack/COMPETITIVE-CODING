memo = [-1] * 100


def fibonacci(i):
    if memo[i] != -1:
        return memo[i]
    if i <= 1:
        return i
    memo[i] = fibonacci(i - 1) + fibonacci(i - 2)
    return memo[i]


if __name__ == "__main__":
    index = int(input())
    re = fibonacci(index)
    print(re)