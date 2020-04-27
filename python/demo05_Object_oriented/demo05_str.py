class Cat:
    def __init__(self, new_name):
        #self.name = "Tom"
        self.name = new_name
    def __del__(self):
        print("Gone")
    def __str__(self):
        return "I'm a cat %s" % self.name
tom = Cat("Tom")
print(tom.name)
print(tom)