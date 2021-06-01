def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1, 1, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

nums = [4, 3, 5, 1, 2]
print(bubble_sort(nums))
