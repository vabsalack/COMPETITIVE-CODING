
def insertion_sor(arr):
    """
    best case time complexity: O(n)
    worst case time complexity: O(n^2)

    """
    size = len(arr)
    for r in range(size):
        current = arr[r]
        l = r - 1
        while l >= 0 and current < arr[l]:
            arr[l + 1] = arr[l]
            l -= 1
        arr[l + 1] = current


if __name__ == "__main__":
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertion_sor(array)
    print(array)

