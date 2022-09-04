
def selection_sort(arr):
    """Time Complexity:
                            Best	O(n2)
                            Worst	O(n2)
                            Space complexity is O(1) """
    size = len(arr)

    for l in range(size):
        min_idx = l
        for r in range(l+1, size):
            if arr[r] < arr[min_idx]:
                min_idx = r

        if l != min_idx:
            arr[l], arr[min_idx] = arr[min_idx], arr[l]


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    selection_sort(array)
    print(array)
