""" https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/ """


def subset_sum(arr):
    n = len(arr)
    res = []
    subset = []

    def sub(i):
        if i == n:
            temp = sum(subset)
            res.append(temp)
        subset.append(arr[i])
        sub(i + 1)
        subset.pop()
        sub(i + 1)

    sub(0)
    return sorted(res)


def small_pos_int(arr):
    arr.sort()
    res = 1
    for i in range(len(arr)):
        if arr[i] <= res:
            res += arr[i]
        else:
            break
    return res


if __name__ == "__main__":
    ar = list(map(int, input().split()))
    # re = small_pos_int(ar)
    re = subset_sum(ar)
    low = 1
    result = 1
    for ele in re:
        if low < ele:
            result = low

    print(re)
