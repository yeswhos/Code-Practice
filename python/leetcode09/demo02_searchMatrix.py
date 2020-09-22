def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    if n == 0 or m == 0:
        return False
    for i in range(n):
        if(target < matrix[i][0]):
            break
        if (matrix[i][m - 1] < target):
            continue
        if (binarySearch(matrix[i], target) == 1):
            return True
    return False

def binarySearch(nums, target):
    start = 0
    ends = len(nums) - 1
    while(start <= ends):
        mid = (start + ends) // 2
        if(nums[mid] < target):
            start = mid + 1
        elif (nums[mid] > target):
            ends = mid - 1
        elif (nums[mid] == target):
            return 1
    return -1

matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
print(searchMatrix(matrix, 21))

