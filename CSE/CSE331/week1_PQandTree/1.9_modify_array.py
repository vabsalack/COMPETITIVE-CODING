from queue import PriorityQueue


def createtarget(target):

    n = len(target)
    sum = 0

    lastsum = 0

    maxheap = PriorityQueue()

    for item in target:
        maxheap.put(-item)

    for i in range(0, n):
        sum += target[i]

    while True:

        lastsum = -maxheap.get()
        sum -= lastsum

        if lastsum == 1 or sum == 1:
            return True
        if lastsum < sum or sum == 0 or lastsum - sum == 0:
            return False

        lastsum -= sum
        sum += lastsum

        maxheap.put(-lastsum)


if __name__ == "__main__":

    n = int(input())
    target = list(map(int, input().split()))

    ans = createtarget(target)

    if ans:
        print("Yes")
    else:
        print("No")


