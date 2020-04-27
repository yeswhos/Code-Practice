class Cat:
    def __init__(self, new_name):
        #self.name = "Tom"
        self.name = new_name
    def __del__(self):
        print("Gone")
tom = Cat("Tom")
print(tom.name)
del tom
print("-------------------------------")