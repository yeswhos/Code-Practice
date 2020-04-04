#递归实现fibonacci
def fibonacci(mounth):
    n1 = 1
    n2 = 1
    n3 = 1

    while(mounth > 2):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        mounth -= 1
    return n3
print(fibonacci(6))