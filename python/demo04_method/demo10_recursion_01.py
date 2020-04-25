def sum(nums):
    if nums == 1:
        return 1
    temp = sum(nums - 1)
    return nums + temp

result = sum(3)
print(result)