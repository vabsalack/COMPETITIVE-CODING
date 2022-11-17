def merge(arr, l, mid, r):

    larr = arr[l: mid + 1]
    rarr = arr[mid + 1: r + 1]

    i = j = 0
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

    mergesort(ar, l, mid)
    mergesort(ar, mid + 1, r)

    merge(ar, l, mid, r)

#############################################################################################


def mergesort1(arr):
    if len(arr) > 1:
        mid = len(arr) >> 1

        l = arr[:mid]
        r = arr[mid:]

        mergesort1(l)
        mergesort1(r)

        i = j = k = 0

        ll, rl = len(l), len(r)

        while i < ll and j < rl:
            if l[i] > r[j]:
                arr[k] = r[j]
                j += 1
            else:
                arr[k] = l[i]
                i += 1

            k += 1

        while i < ll:
            arr[k] = l[i]
            i += 1
            k += 1

        while j < rl:
            arr[k] = r[j]
            j += 1
            k += 1


if __name__ == "__main__":
    ar = [-5, 9, 0, 4, -10, 100]
    # mergesort(arr, 0, len(arr) - 1)
    mergesort1(ar)
    print(ar)
