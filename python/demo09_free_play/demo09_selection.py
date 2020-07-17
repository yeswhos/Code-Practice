def selection(list):
    n = len(list)
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if(list[min] > list[j]):
                min = j
        list[i], list[min] = list[min], list[i]

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection(list)
print(list)