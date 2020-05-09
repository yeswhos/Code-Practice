class Dog(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print("%s 玩" % self.name)

class XiaoTian(Dog):
    def game(self):
        print("%s 玩" % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name
    def game_with_dog(self, dog):
        print("%s与 %s玩" % (self.name, dog.name))

wangCai = Dog("wangcai")
ming = Person("ming")
ming.game_with_dog(wangCai)