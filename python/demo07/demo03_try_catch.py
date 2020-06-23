try:
    num = int(input("input a integer: "))
    result = 8 / num;
    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确的整数")