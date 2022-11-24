def waveFormArray(arr, n):

    f = 1
    for i in range(len(arr) - 1):
        if f == 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        elif f == 0 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        f = 1 - f
#         print(arr)
    return arr


if __name__ == "__main__":
    ar = [4, 3, 2, 5, 4, 1]
    waveFormArray(ar)
    print(ar)