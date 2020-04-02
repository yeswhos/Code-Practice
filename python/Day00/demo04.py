def funA(x, y = 3):
    return x * y

print(funA(3))

print(lambda x, y : x * y)

g = lambda x, y : x * y
print(g(3, 3))