import random


class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.progress += 0.50
        self.gladness -= 3
    def to_sleep(self):
        print("It is too late (time to sleep)")
        self.progress -= 0.25
        self.gladness += 2

    def to_chill(self):
        print("I need a little break")
        self.progress -= 0.25
        self.gladness += 4

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out......(you lose)")
            self.alive = False
        elif self.gladness < 0:
            print("Depression (you lose)")
            self.alive = False
        elif self.progress > 10:
            print("You finished a IT STEP!!!! (You WIN!!)")

    def end_of_day(self):
        print("End of a day")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
    def live(self, day):
        d = "Day " + str(day) + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_study()
        if live_cube == 2:
            self.to_chill()
        if live_cube == 3:
            self.to_sleep()
        if live_cube == 4:
            self.to_study()
        self.end_of_day()
        self.is_alive()

name = input("Input Name > ")
jora = Student(name=name)
for i in range(366):
    if jora.alive == False:
        break
    jora.live(i)


