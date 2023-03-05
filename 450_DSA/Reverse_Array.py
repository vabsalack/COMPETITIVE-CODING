""" https://practice.geeksforgeeks.org/problems/reverse-an-array/0 """
"""commit check"""

def main(A, N):
    limit = N // 2
    for i in range(0, limit):
        A[i] = A[i] + A[N - 1 - i]
        A[N - 1 - i] = A[i] - A[N - 1 - i]
        A[i] = A[i] - A[N - 1 - i]

    print(*A)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().split()))
        main(A, N)