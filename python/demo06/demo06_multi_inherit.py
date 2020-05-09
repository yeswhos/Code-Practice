class A:
    def demo(self):
        print("self方法")

class B:
    def test(self):
        print("test 方法")

class C(A, B):
    pass

c = C()
c.demo()
c.test()