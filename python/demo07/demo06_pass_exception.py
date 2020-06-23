def demo01():
    return int(input("input integer: "))

def demo02():
    return demo01()
try:
    print(demo02())
except Exception as result:
    print(result)