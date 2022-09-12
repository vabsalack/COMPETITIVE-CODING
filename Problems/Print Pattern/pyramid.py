
def pyramid_pat(x):
    for i in range(x - 1, -1, -1):
        print(" "*i + "* "*(x - i))


def left_triangle(x):
    for i in range(1, x + 1):
        for j in range(i):
            print("x", end=" ")
        print()


def right_triangle(x):
    for i in range(x-1, -1, -1):
        for j in range(x):
            if j >= i:
                print("x", end=" ")
            else:
                print(" ", end=" ")
        print()


def palindrome(s):
    m = len(s) // 2
    for i in range(m + 1):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def palindrome_num(x):
    y = x
    rx = 0
    while x:
        temp = x % 10
        x = x // 10
        rx = rx*10 + temp
    if y == rx:
        return True
    return False


left_triangle(5)
right_triangle(5)
print(palindrome_num(1331))





