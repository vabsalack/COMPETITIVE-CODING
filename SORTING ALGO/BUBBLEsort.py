def bubble_sort(arr):
    """
     Time Complexities:
        Worst Case Complexity: O(n2)
        Best Case Complexity: O(n)

    Space Complexity:
        optimized bubble sort algorithm: O(2)
    """
    length = len(arr)
    for j in range(length):
        swapped = True

        for i in range(0, length - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = False

        if swapped:
            break

    return


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(array)
    print(array)



