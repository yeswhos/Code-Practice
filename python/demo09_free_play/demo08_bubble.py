def bubble(list):
    n = len(list)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            counter = 0
            if(list[j] > list [j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
                counter += 1
        if counter == 0:
            return

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble(list)
print(list)