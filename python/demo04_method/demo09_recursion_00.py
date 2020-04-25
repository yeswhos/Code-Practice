def demo(num):
    print(num)
    num -= 1
    if (num == 1):
        return
    demo(num)
demo(3)