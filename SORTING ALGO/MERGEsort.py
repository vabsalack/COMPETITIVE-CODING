def merge(arr, l, mid, r):

    larr = arr[l: mid + 1]
    rarr = arr[mid + 1: r + 1]

    i = j = k = 0
    k = l
    len_l, len_r = len(larr), len(rarr)

    while i < len_l and j < len_r:
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1

        k += 1

    while i < len_l:
        arr[k] = larr[i]
        i += 1
        k += 1

    while j < len_r:
        arr[k] = rarr[j]
        j += 1
        k += 1


def mergesort(ar, l, r):
    if l == r:
        return

    mid = (l + r) >> 1

    mergesort(arr, l, mid)
    mergesort(arr, mid + 1, r)

    merge(arr, l, mid, r)


if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5]
    mergesort(arr, 0, len(arr) - 1)
    print(arr)