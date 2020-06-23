try:
    num = int(input("input a integer: "))
    result = 8 / num;
    print(result)
except Exception as result:
    print("Unkown error %s" % result)