def heap_sort(arr, r):
    size = r + 1
    if size > 1:
        for i in range((size//2 - 1), -1, -1):
            heapify(arr, size, i)
        arr[0], arr[r] = arr[r], arr[0]
        heap_sort(arr, r - 1)


def heapify(arr, n, i):

    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


if __name__ == "__main__":
    array = [6, 4, 3, 8, 9, 1, 3, 7, 8]
    heap_sort(array, len(array)-1)
    print(array)