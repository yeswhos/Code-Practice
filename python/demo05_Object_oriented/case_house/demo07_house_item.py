class HouseItem:
    def __init__(self, name, size):
        self.name = name;
        self.size = size;
    def __str__(self):
        return "[%s] occupy %.2f room" % (self.name, self.size)

bed = HouseItem("席梦思", 10)
table = HouseItem("餐桌", 4)

# print(bed)
# print(table)

