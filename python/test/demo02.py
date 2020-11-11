def findVal(m, n, k):
    # m, n = str(m), str(n)
    # print(list(str(m) + str(n))
    return sorted(m + n).index(k - 1)

m = [1,2,2,7]
n = [3,4,5]
k = 5
print(findVal(m, n, k))