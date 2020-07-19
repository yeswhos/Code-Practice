def quick(list, first, last):
    if(first >= last):
        return
    high = last
    low = first
    mid_value = list[first]

    while low < high:
        while ((low < high) and (list[high] >= mid_value)):
            high -= 1
        list[low] = list[high]

        while ((low < high) and (list[low] < mid_value)):
            low += 1
        list[high] = list[low]

    list[low] = mid_value
    quick(list, first, low - 1)
    quick(list, low + 1, last)

if __name__ == "__main__":
    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick(list, 0, len(list) - 1)
    print(list)