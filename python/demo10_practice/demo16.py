li = [0, 8, 4, 12, 2]

def fn(a):
    res = []
    for item in a[::-1]:
        if not res or item > res[-1]:
            res.append(item)
        else:
            left = 0
            right = len(res) - 1
            loc = right
            while left <= right:
                mid = (left + right) // 2
                if item < res[mid]:
                    right = mid - 1
                else:
                    loc = mid
                    left = mid + 1
            res[loc] = item
    print(res)
    return len(res)
print(fn(li))