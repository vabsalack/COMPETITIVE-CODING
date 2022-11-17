def mergesort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l, r = arr[:m], arr[m:]

        mergesort(l)
        mergesort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1

            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    mergesort(nums)
    print("[", end="")
    print(*nums, sep=",", end="")
    print("]")