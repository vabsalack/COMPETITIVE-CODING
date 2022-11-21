# Enter your code here. Read input from STDIN. Print output to STDOUT
def partition(ar):
    if len(ar) < 2:
        return ar
    p = ar[0]
    smaller = [x for x in ar[1:] if x < p]
    bigger = [x for x in ar[1:] if x >= p]
    return smaller, p, bigger


def quickSort(ar):
    if len(ar) < 2:
        return ar
    (smaller, p, bigger) = partition(ar)
    res = quickSort(smaller) + [p] + quickSort(bigger)
    print(*res, sep=" ")
    return res


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    quickSort(nums)
