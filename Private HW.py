import random


class Numbers:
    def __init__(self):
        self.__number1 = 22
        self.__number2 = 11

    def plus(self):
        e = self.__number1 =+ self.__number2
        print(e)

    def minus(self):
        e = self.__number1 =- self.__number2
        print(e)

    def umnog(self):
        e = self.__number1 * self.__number2
        print(e)

    def podel(self):
        e = self.__number1 // self.__number2
        print(e)

        ran = random.randint(1,4)
        if ran == 1:
            self.plus()
        elif ran == 2:
            self.minus()
        elif ran == 3:
            self.umnog()
        elif ran == 4:
            self.podel()
