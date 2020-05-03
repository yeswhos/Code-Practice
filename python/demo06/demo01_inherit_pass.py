class Animal:
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")

class Dog(Animal):
    def bark(self):
        print("bark")

class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")

xiaotianquan = XiaoTianQuan()
xiaotianquan.fly()
xiaotianquan.eat()
xiaotianquan.drink()