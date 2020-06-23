try:
    num = int(input("input a integer: "))
    result = 8 / num;
    print(result)
except Exception as result:
    print("错误 %s" %result)
finally:
    print("finally")