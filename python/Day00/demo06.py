print((list(map(lambda x, y : [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))))
def combine(x, y):
    z = zip(x, y)
    return z
############################################
x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]
print(list(combine(x, y)))