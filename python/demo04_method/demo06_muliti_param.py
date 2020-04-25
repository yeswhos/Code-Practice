def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, 5, name = "Fanhui", age = 23)