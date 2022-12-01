#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin

"""
小明今年18 岁，身高 1.75，每天早上跑完步，会去吃东西
小美今年17 岁，身高 1.65，小美不跑步，小美喜欢吃东西
"""


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age
        print('{}今年{}岁，身高{}'.format(self.name, self.age, self.height))

    def preferRunning(self):
        print("喜欢跑步，跑完步后会去" + self.eatFood())

    def noRunning(self):
        print("不跑步，喜欢" + self.eatFood())

    def eatFood(self):
        return "吃东西"


Person('小明', '18', '1.75').preferRunning()
Person('小美', '17', '1.65').noRunning()