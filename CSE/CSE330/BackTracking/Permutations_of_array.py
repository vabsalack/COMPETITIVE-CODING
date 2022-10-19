def permute(arr):
    res = []

    if len(arr) == 1:
        return [arr[:]]

    for i in range(len(arr)):
        n = arr.pop(0)
        p = permute(arr)

        for pp in p:
            pp.append(n)

        res.extend(p)
        arr.append(n)

    return res


if __name__ == "__main__":
    ar = list(map(int, input().split()))
    re = permute(ar)
    print(*re, sep="\n")