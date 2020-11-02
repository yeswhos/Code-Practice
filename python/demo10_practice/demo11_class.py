class A(object):
    def go(self):
        print("A go")
    def stop(self):
        print("A stop")
    def pause(self):
        raise Exception("Not being implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("B go")

class C(A):
    def go(self):
        super(C, self).go()
        print("C go")
    def stop(self):
        super(C, self).stop()
        print("C stop")

class D(B, C):
    def go(self):
        super(D, self).go()
        print("D go")
    def stop(self):
        super(D, self).stop()
        print("D stop")
    def pause(self):
        print("D wait")

class E(B, C):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()

d.go()
# e.go()