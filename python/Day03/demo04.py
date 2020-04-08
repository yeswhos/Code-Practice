#递归实现bin()功能，自制
# a = 4
# print(bin(a))

def binary(num):
    num = int(num)
    #print(num)
    if (num % 2 == 0) & (num != 0):
        print("0")
        return binary(num / 2)
    elif (num % 2 == 1) & (num != 1):
        print("1")
        return binary(num / 2)
    elif num == 1:
        print("1")
    elif num == 0:
        print("0")
    
    
print(binary(4))