def binary_search(list, item):
    n = len(list)
    mid = n / 2
    if(list[mid] == item):
        return True
    elif(mid >=1):
        if(list[mid] < item):
            return binary_search(list[mid + 1:], item)
        else:
            return binary_search(list[:mid], item)
    return False

