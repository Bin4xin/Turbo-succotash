#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin

"""
有一个房子，和一些家具
房子：户型，面积
家具：
    - 床，  4平米
    - 衣柜，2平米
    - 餐桌，1.5平米
把家具放到房子里后，打印房子的户型，总面积，剩余面积，家具。
- if judge.
- add Furniture to House <class>.
"""


class House:
    def __init__(self, area, type):
        self.area = area
        self.type = type
        # add some var:
        self.preArea = area
        self.FurnitureList = []

    # new. 封装添加家具方法，初始化家具时可以直接调用。
    def addFurniture(self, Furnitures):
        if Furnitures.m2 > self.preArea:
            print("Sorry, your House are not big enough to set your furnitures.")
            return
        self.FurnitureList.append(Furnitures.name)
        self.preArea = self.preArea - Furnitures.m2

    def pop_of_Houst(self):
        print("{}一共{}平米，装完家具还有{}平米，装的家具是：{}".format(self.type,
                                                                     self.area,
                                                                     self.preArea,
                                                                     self.FurnitureList))


class Furniture:
    def __init__(self, name, m2):
        self.name = name
        self.m2 = m2


bed = Furniture("床", 4)
wardrobe = Furniture("衣柜", 2)
lunch_table = Furniture("餐桌", 1.5)

my_house = House(100, "小平楼")
# add. 向房子里添加家具
my_house.addFurniture(bed)
my_house.addFurniture(wardrobe)
my_house.addFurniture(lunch_table)
my_house.pop_of_Houst()

big_house = House(1000, "别墅")
big_house.addFurniture(bed)
big_house.addFurniture(wardrobe)
big_house.addFurniture(lunch_table)
big_house.pop_of_Houst()

small_house = House(5.5, "狗窝")
small_house.addFurniture(bed)
small_house.addFurniture(wardrobe)
small_house.addFurniture(lunch_table)
small_house.pop_of_Houst()