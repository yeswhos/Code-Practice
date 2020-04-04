#递归求幂
def power(x, y):
    if x == 0:
        return 0
    elif y== 0:
        return 1
    else:
        return power(x, y - 1) * x

print(power(2, 2)) 