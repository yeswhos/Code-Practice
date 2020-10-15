def singNumber(nums):
    r = 0
    for item in nums:
        r ^= item
    return r

nums = [2, 2, 1]
print(singNumber(nums))