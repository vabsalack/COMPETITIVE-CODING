def find_length(n):
    temp = n
    count = 0
    num = []
    while temp:
        num.append(temp % 10)
        count += 1
        temp = temp // 10
    return count, num[::-1]


print(find_length(15666))