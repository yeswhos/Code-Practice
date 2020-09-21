def feb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)

print(feb(6))
