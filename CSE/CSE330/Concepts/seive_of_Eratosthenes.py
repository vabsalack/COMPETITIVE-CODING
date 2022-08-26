import math


def check_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, math.floor(math.sqrt(x))+1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


def naive_method(n):
    """ to find all prime number up to n
        time complexity for this one is O(n*)"""
    result = []
    for i in range(2, n+1):
        if check_prime(i):
            result.append(i)
    return result


def sieve_of_eratosthenes(n):
    """ by using sieve of eratosthenes the time complexity is o(nlog(log(n)))"""
    p = [1]*(n+1)
    for i in range(2, n+1):
        if p[i] == 1:
            for j in range(i+i, n+1, i):
                p[j] = 0

    for i in range(2, len(p)):
        if p[i] == 1:
            print(i, end=" ")


if __name__ == "__main__":
    x = int(input("> "))
    res = naive_method(x)
    print(*res)
    sieve_of_eratosthenes(x)

