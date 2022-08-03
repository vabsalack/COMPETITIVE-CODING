def find_remain(dividend, divisor):

    if dividend >= divisor:
        mul = 1
        temp = divisor * mul
        while temp <= dividend:
            mul += 1
            temp = divisor * mul
        temp = divisor * (mul - 1)
        print(dividend - temp)
    else:
        print(dividend)


if __name__ == "__main__":
    find_remain(46, 3)