from timeit import Timer


def test00():
    list = []
    for i in range(10000):
        list.append(i)

def test01():
    list = []
    for i in range(10000):
        list += i

def test02():
    list = [i for i in range(10000)]

def test03():
    list = list(range(10000))

timer1 = Timer("test00()", "from __main__ import test00")
print(timer1.timeit(1000))