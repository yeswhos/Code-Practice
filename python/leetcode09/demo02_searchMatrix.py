def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    i = 0
    j = 0
    counter = 0
    while (target != matrix[i][j]):
        if target > matrix[i][j]:
            j += 1
        if target < matrix[i][j]:
            j = j - 1
        if target > matrix[i][j]:
            i += 1
        if target < matrix[i][j]:
            i = j - 1
        counter += 1
        if counter >= m * n:
            return False
    return True

matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
print(searchMatrix(matrix, 20))

