def shell(list):
    n = len(list)
    gap = n // 2
    while (gap > 0):
        for i in range (gap, n):
            j = i
            while (j > 0):
                if (list[j] < list[j - gap]):
                    list[j], list[j - gap] = list[j - gap], list[j]
                    j -= gap
                else:
                    break
            i += 1
        gap = gap // 2

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell(list)
print(list)