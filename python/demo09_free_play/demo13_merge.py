def merge(list):
    n = len(list)
    midValue = n // 2
    if (n <= 1):
        return list
    right_list = merge(list[:midValue])
    left_list = merge(list[midValue:])

    left_pointer, right_pointer = 0, 0
    res = []
    while(left_pointer > len(left_list)) and (right_pointer > len(right_list)):
        if(left_list[left_pointer] < list[right_list]):


