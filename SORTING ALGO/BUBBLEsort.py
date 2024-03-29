

def bubble_sort(arr):
    """
         Time Complexities:
            Worst Case Complexity: O(n2)
            Best Case Complexity: O(n)

        Space Complexity:
            optimized bubble sort algorithm: O(2)
        """

    length = len(arr)
    for i in range(length - 1, 0, -1):
        swapped = True

        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = False

        if swapped:
            break
    return


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(array)
    print(array)



