def binary_search(list, item):
    n = len(list)
    mid = n // 2
    if (n > 0):
        if(list[mid] == item):
            return True
        if(list[mid] < item):
            return binary_search(list[mid + 1:], item)
        else:
            return binary_search(list[:mid], item)
    return False

if __name__ == "__main__":
    list = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(list, 100))