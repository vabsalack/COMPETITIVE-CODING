
def selection_sort(arr):
    """Time Complexity:
                        Best	O(n2)
                        Worst	O(n2)
                        Space complexity is O(1) """
    size = len(arr)

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i

        arr[step], arr[min_idx] = arr[min_idx], arr[step]


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    selection_sort(array)
    print(array)
