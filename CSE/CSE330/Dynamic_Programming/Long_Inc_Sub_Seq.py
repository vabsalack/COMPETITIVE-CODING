from bisect import bisect_left as bl


def longestIncreasingSubsequence(arr):
    # solution using binary search O(n*log(n))
    sub = []
    for x in arr:

        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)

        else:

            idx = bl(sub, x)
            sub[idx] = x

    return len(sub)


def LIS(arr):
    # dynamic solution
    length = len(arr)
    dp = [1] * length

    for i in range(length-1, -1, -1):
        for j in range(i + 1, length):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)
