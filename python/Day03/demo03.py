#汉诺塔
def haino(n, x, y, z):
    if n == 1:
        print(x, '->', z)
    else:
        haino(n - 1, x, z, y)
        print(x, '->', z)
        haino(n - 1, y, x, z)
        #print(y, '->', z)

haino(3, 'X', 'Y', 'Z')