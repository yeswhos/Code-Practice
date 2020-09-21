def singleNumber(nums):
    n = len(nums)
    r = 0
    for i in range(n):
        #异或XOR运算，相同为0，相异为1
        r = r ^ nums[i]
    return r

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))