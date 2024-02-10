# class Human:
#     height = 180
#
# class Student(Human):
#     satiety = 100
# class Worker(Human):
#     satiety = 30
#
# nick = Student()
# anna = Worker()
# print(nick.height)
# print(anna.height)
# print(nick.satiety)
# print(anna.satiety)
#
#
# class GrandParents:
#     height = 160
#     satiety = 100
#     age = 68
#
# class Parents(GrandParents):
#     age = 40
#
# class Child(Parents):
#     height = 100
#     age = 5
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)

class Hello_World:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "World" # public
        self._world = "_World" # protected - захищений
        self.__world = "__World" # private
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
class Hi(Hello_World):
    def hi_printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

h = Hello_World()
h.printer()
hi = Hi()
hi.hi_printer()