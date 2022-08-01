from MergeSort import mergesort


def main(array):
    mergesort(array)
    print(array)


if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #  output is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    main(arr)