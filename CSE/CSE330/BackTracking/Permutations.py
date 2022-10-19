def permute(nums):
    re = []
    # base case
    if len(nums) == 1:
        return [nums[:]]

    # main logic
    for i in range(len(nums)):
        temp = nums.pop(0)
        perms = permute(nums)

        for per in perms:
            per.append(temp)

        re.extend(perms)
        nums.append(temp)

    return re


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    resu = permute(arr)
    print(len(resu), "\n", resu)

