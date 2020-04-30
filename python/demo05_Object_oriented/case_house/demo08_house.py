from case_house.demo07_house_item import HouseItem, bed


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []
    def __str__(self):
        return "户型： %s \n总面积: %2f, 剩余: %2f \n家具: %s"\
               % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        print("添加 %s" % item)

my_home = House("Flat", 150)
my_home.add_item(bed)
print(my_home)
