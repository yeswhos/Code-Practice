def demo(*args, **kwargs):
    print(args)
    print(kwargs)

a = (1, 2, 3, 4, 5)
b = {"name" : "Fanhui", "age" : 18}
demo(*a, **b)