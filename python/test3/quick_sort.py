def quick_sort(nums, first, last):
    if first >= last:
        return nums
    n = len(nums)
    low = first
    high = last
    mid = nums[first]
    while low < high:
        while low < high and nums[high] >= mid:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < mid:
            low += 1
        nums[high] = nums[low]
    nums[low] = mid
    quick_sort(nums, first, low - 1)
    quick_sort(nums, low + 1, last)

nums = [4, 3, 5, 1, 2]
quick_sort(nums, 0, len(nums)-1)
print(nums)