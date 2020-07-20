def merge(alist):
    n = len(alist)

    if(n <= 1):
        return alist
    mid = n // 2
    left_list = merge(alist[:mid])
    right_list = merge(alist[mid:])

    left_pointer, right_pointer = 0, 0
    res = []
    while(left_pointer < len(left_list)) and (right_pointer < len(right_list)):
        if left_list[left_pointer] < right_list[right_pointer]:
            res.append(left_list[left_pointer])
            left_pointer += 1
        else:
            res.append(right_list[right_pointer])
            right_pointer += 1
    # res.append(left_list[left_pointer:])
    # res.append(right_list[right_pointer:])
    res += left_list[left_pointer:]
    res += right_list[right_pointer:]
    return res

if __name__ == "__main__":
    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    list = merge(list)
    print(list)
