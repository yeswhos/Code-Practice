def binary_search_v2(list, item):
    #迭代
    n = len(list)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if(list[mid] == item):
            return True
        elif(list[mid] > item):
            last = mid - 1
        elif(list[mid] < item):
            first = mid + 1
    return False

if __name__ == "__main__":
    list = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search_v2(list, 100))
    print(binary_search_v2(list, 55))