mem = []


def main(n):
    if len(mem)-1 > n:
        return mem[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    total = main(n - 1) + main(n - 2)
    mem.append(total)
    return total


def print_fs(n):
    array = [0, 1]
    while len(array) < n:
        array.append(array[-1]+array[-2])
    print(*array)


"""0 1 1 2 3 5 8 13"""

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    for i in arr:
        main(i)
    print(mem)
