nums = [3, 34, 4, 12, 5, 2]
target = 9
def recursion(arr, i, target):
    if i == 0:
        return arr[0] == target
    elif target == 0:
        return True
    elif arr[i] > target:
        return recursion(arr, i - 1, target)
    else:
        A = recursion(arr, i - 1, target - arr[i])
        B = recursion(arr, i - 1, target)
        return A or B

print(recursion(nums, len(nums) - 1, target))