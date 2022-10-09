def kFactorization(n, A):
    # Write your code here

    def recursion(n, A):
        if n == 1:
            return []

        for x in A:
            if n % x == 0:
                result = recursion(n // x, A)
                if result is not False:
                    result.append(x)
                    return result
        else:
            return False

    A.sort(reverse=True)
    result = recursion(n, A)

    re = []

    if result is False:
        return [-1]

    else:

        re.append(1)
        current = 1
        for x in result:
            current *= x
            re.append(current)

    return re
