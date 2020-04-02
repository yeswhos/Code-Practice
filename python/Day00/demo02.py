#filter()
def odd(x):
    return x % 2
x = range(10)
print(list(filter(odd, x)))