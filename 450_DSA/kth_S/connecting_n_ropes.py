
def heapify(array, i, n):

    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and array[left] < array[smallest]:
        smallest = left
    if right < n and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[smallest], array[i] = array[i], array[smallest]
        heapify(array, smallest, n)

result = []
"""
def main(arr):
    for _ in range(2):
        for i in range(len(arr)//2 - 1, -1, -1):

"""
if __name__ == "__main__":
    main()