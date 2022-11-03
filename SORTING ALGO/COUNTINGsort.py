def counting_sort(arr):
    size = len(arr)
    output = [0] * (size)
    maxi = arr[0]
    for i in range(1, size):
        maxi = max(maxi, arr[i])

    count = [0] * (maxi + 1)

    for i in range(size):
        count[arr[i]] += 1

    for i in range(1, maxi + 1):
        count[i] += count[i - 1]


