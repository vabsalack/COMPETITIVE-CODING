def partition(ar, l, r):
    pivot = ar[r]

    down = l - 1

    for up in range(l, r+1):

        if ar[up] <= pivot:
            down += 1
            ar[up], ar[down] = ar[down], ar[up]

    return down


def quicksort_ll(ar, l, r):
    """ this quicksort is considering pivot element in last index"""

    if l > r:
        return

    pi = partition(ar, l, r)
    quicksort_ll(ar, l, pi - 1)
    quicksort_ll(ar, pi + 1, r)

######################################################################


def partition1(ar, first, last):
    l = first
    r = last

    while l != r:
        if ar[r] >= ar[l]:
            r -= 1
        elif ar[l + 1] <= ar[l]:
            ar[l + 1], ar[l] = ar[l], ar[l + 1]
            l += 1
        else:
            ar[l + 1], ar[r] = ar[r], ar[l + 1]

    return l


def quicksort_fl(ar, first, last):
    if first >= last:
        return
    position = partition1(ar, first, last)
    quicksort_fl(ar, first, position - 1)
    quicksort_fl(ar, position + 1, last)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    quicksort_ll(arr, 0 , len(arr) - 1)
    print(arr)


