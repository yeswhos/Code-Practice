def feb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)

print(feb(6))

list = list()
for i in range(1, 7):
    list.append(feb(i))
    print(list)

