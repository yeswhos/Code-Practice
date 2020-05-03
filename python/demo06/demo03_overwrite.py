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
    def bark(self):
        print("overwrite bark")

xtq = XiaoTianQuan()
xtq.bark()