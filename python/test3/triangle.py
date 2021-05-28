def generate(nums):
    res = []
    for i in range(nums):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(res[i-1][j-1] + res[i-1][j])
        res.append(temp)
    return res

print(generate(5))
