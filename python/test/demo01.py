def multiplyMartix(A, B):
    res = [[0 for i in range(len(A[0]))] for j in range(len(B))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for n in range(len(A[0])):
                res[i][j] += A[i][j] * B [j][n]
    return res[:2]
A, B = [[1,0,0],[-1,0,5]],[[6,0,0],[0,0,0],[0,0,1]]
print(multiplyMartix(A, B))