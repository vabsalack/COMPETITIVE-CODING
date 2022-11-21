# Enter your code here. Read input from STDIN. Print output to STDOUT
def printt(ar, n):
    for i in range(n):
        print(ar[i], end=" ")
    print()


def partition(arr, l, r, n):
    pivot = arr[r]
    down = l - 1
    for i in range(l, r + 1):
        if arr[i] <= pivot:
            down += 1
            arr[down], arr[i] = arr[i], arr[down]
    printt(arr, n)
    return down


def quicksort(arr, l, r, n):
    if l < r:
        index = partition(arr, l, r, n)
        quicksort(arr, l, index - 1, n)
        quicksort(arr, index + 1, r, n)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    quicksort(nums, 0, n - 1, n)