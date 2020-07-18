def insert_sort(list):
    n = len(list)
    for i in range(1, n):
        j = i
        while j > 0:
            if (list[j] < list[j - 1]):
                list[j], list[j - 1] = list[j - 1], list[j]
                j -= 1
            else:
                break

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(list)
print(list)