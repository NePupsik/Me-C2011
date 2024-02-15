import random

class Players:
    def __init__(self, roleP, name, roleP1, name1, roleP2, name2, roleP3, name3):
        self.roleP = roleP
        self.name = name
        self.roleP1 = roleP1
        self.name1 = name1
        self.roleP2 = roleP2
        self.name2 = name2
        self.roleP3 = roleP3
        self.name3 = name3

    role = random.randint(1,4)
    if role == 1:
        roleP = "Мирный"
    elif role == 2:
        roleP = "Мирный"
    elif role == 3:
        roleP = "Шериф"
    elif role == 4:
        roleP = "Мафия"

    name = input("Input first Name > ")
    print(f"{name}'s role = {roleP}")

    name1 = input("Input second Name > ")
    print(f"{name1}'s role = {roleP1}")

    name2 = input("Input third Name > ")
    print(f"{name2}'s role = {roleP2}")

    name3 = input("Input fourth Name > ")
    print(f"{name3}'s role = {roleP3}")