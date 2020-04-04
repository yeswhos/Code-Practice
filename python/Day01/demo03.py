#递归实现fibonacci数列，镜像代码demo04
def fibonacci(mounth):
    if mounth == 1:
        return 1
    elif mounth == 2:
        return 1
    elif mounth == 3:
        return 2
    else:
        return fibonacci(mounth - 1) * fibonacci(mounth - 2)

print(fibonacci(6))