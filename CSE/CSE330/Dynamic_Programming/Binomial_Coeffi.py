def binomial_coefficient(x, y):

    def BC(n, k):
        if dp[n][k] != -1:
            return dp[n][k]
        else:
            for i in range(n + 1):
                for j in range(k + 1):
                    if j == 0 or j == i:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = BC(i - 1, j - 1) + BC(i - 1, j)

            return dp[n][k]

    return BC(x, y)


if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    dp = [[-1] * (a + 1)] * (b + 1)
    re = binomial_coefficient(a, b)
    print(re)
