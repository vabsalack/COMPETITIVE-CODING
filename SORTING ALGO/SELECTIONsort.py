'''https://practice.geeksforgeeks.org/problems/selection-sort/1/#'''

def select(arr, i):
    # code here
    min_idx = i
    for j in range(i, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    return min_idx


def selectionSort(arr, n):
    length = len(arr)
    for i in range(length):
        j = select(arr, i)
        # tmp = arr[i]
        # arr[i] = arr[j]
        # arr[j] = tmp
        if i == j:
            continue
        arr[i] = arr[i] + arr[j]
        arr[j] = arr[i] - arr[j]
        arr[i] = arr[i] - arr[j]
    return arr


if __name__ == "__main__":
    arr = list(map(int, input("enter array elements: ").split()))
    sorted_arr = selectionSort(arr, len(arr))
    print(sorted_arr)
