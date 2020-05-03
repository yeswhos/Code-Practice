class Animal:
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")

class Dog(Animal):
    # def eat(self):
    #     print("eat")
    # def drink(self):
    #     print("drink")
    def bark(self):
        print("bark")

dog = Dog()
dog.eat()
dog.drink()
dog.bark()
