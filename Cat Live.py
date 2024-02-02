import random


class Cat:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 20
        self.alive = True

    def to_eat(self):
        print("Time to eat!")
        self.satiety += 2
        self.gladness += 1
    def to_sleep(self):
        print("It is too late (time to sleep)")
        self.satiety -= 2
        self.gladness += 1

    def to_pLay(self):
        print("I need to play!!!")
        self.satiety -= 3
        self.gladness += 4

    def is_alive(self):
        if self.satiety < 0:
            print("died of hunger (you lose)")
            self.alive = False
        elif self.gladness < 0:
            print("Depression (you lose)")
            self.alive = False
        elif self.satiety > 30:
            print("Your cat is happy!!!! (You WIN!!)")

    def end_of_day(self):
        print("End of a day")
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {self.satiety}")
    def live(self, day):
        d = "Day " + str(day) + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_eat()
        if live_cube == 2:
            self.to_pLay()
        if live_cube == 3:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()

name = input("Input cat's Name > ")
cat = Cat(name=name)
for i in range(366):
    if cat:
        cat.alive == False
        break
    cat.live(i)