def find_subsets(arr):
    result = []
    subset = []

    def dfs(i):
        if i == len(arr):
            result.append(subset.copy())
            return

        #  decision to include arr[i]
        subset.append(arr[i])
        dfs(i+1)

        #  decision not to include arr[i]
        subset.pop()
        dfs(i+1)

    dfs(0)

    return result


if __name__ == "__main__":
    arr = [1, 2, 3]
    final = find_subsets(arr)
    print(*final, sep="\n")

