def toh(n, src, hlp, des):
    global move

    if n == 0:
        return

    toh(n - 1, src, des, hlp)
    move += 1
    print(f"Moving ring {n} from {src} to {des} : move {move}")
    toh(n - 1, hlp, src, des)


if __name__ == "__main__":
    n = int(input())
    source, helper, destination = list(input().strip().split())
    move = 0
    toh(n, source, helper, destination)

