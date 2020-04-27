class Person:
    def __init__(self, name, weight):
        #属性 = 形参
        self.name = name
        self.weight = weight
    def __str__(self):
        return "名字: %s , 体重: %.2f "% (self.name, self.weight)
    def run(self):
        print("run")
        self.weight -= 0.5
    def eat(self):
        print("eat")
        self.weight += 1

fanhui = Person("Fanhui", 130.0)
fanhui.run()
fanhui.eat()
print(fanhui)