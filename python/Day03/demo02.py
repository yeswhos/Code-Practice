#递归梅开二度
def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num == 3:
        return 2
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(12))