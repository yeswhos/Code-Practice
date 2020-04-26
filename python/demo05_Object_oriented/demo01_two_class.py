class Cat:
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")

tom = Cat()
print(tom)
lazy_tom = Cat()
print(lazy_tom)
lazy = lazy_tom
print(lazy)