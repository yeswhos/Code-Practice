#递归实现bin()功能，官方答案
#妙啊
def binary(num):
    result = ""
    if num:
        result = binary(num // 2)
        return result + str(num % 2)
    else:
        return result

print(binary(10))