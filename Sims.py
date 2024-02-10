import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 700
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def eat(self):
        if self.home.food <= 0:
            print("Oh no!")
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            else:
                print("I want to eat!")
                self.satiety += 5
                self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                print("Oh no!")
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        print("Time to work! :)")
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -=5
    def shopping(self, manage):
        print("Time to shopping")
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel!")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bough food!")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("I'm happy!!")
            self.money -= 20
            self.gladness += 10
            self.satiety += 5
    def clean_home(self):
        print("Time to do a chores!")
        self.home.mess = 0
    def get_work(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def get_car(self):
        self.car = Auto(brand_of_car)
    def get_home(self):
        self.home = House()
    def chill(self):
        print("Time to chill!")
        self.gladness += 15
        self.home.mess += 7
        self.home.food -= 5
    def to_repair(self):
        print("Time to repair my car!")
        self.car.strength += 120
        if brand_of_car == "BMW":
            if self.car.strength > 100:
                self.car.strength = 100
        elif brand_of_car == "Lada":
            if self.car.strength > 20:
                self.car.strength = 20
        elif brand_of_car == "Volvo":
            if self.car.strength > 120:
                self.car.strength = 120
        elif brand_of_car == "Ferrari":
            if self.car.strength > 80:
                self.car.strength = 80
    def day_indexes(self, day):
        d = f"Today the {day} of {self.name}'s live"
        print(f"{d:=^50}\n")
        h_i = f"{self.name}'s indexes"
        print(f"{h_i:-^50}\n")
        print(f"Gladness: {self.gladness}")
        print(f"Satiety: {self.satiety}")
        print(f"Money: {self.money}")
        home_i = "Home indexes"
        print(f"{home_i:-^50}\n")
        print(f"Food: {self.home.food}")
        print(f"Mess: {self.home.mess}")
        car_i = f"{self.car.brand} car indexes"
        print(f"{car_i:-^50}\n")
        print(f"Brand: {self.car.brand}")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")
        print(f"Cons: {self.car.cons}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead (of hunger)...")
        if self.money < -100:
            print("Bankrupt...")
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("I am not a БОМЖ anymore!!")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a {self.car.brand}!")
        if self.job is None:
            self.get_work()
            print(f"I am working a {self.job.job} and my salary is {self.job.salary}!")
            self.day_indexes(day)
            dice = random.randint(1,4)
            if self.satiety < 20:
                self.eat()
            elif self.gladness < 20:
                self.chill()
            elif self.money < 2:
                self.work()
            elif self.car.strength < 10:
                self.to_repair()
            elif dice == 1:
                self.chill()
            elif dice == 2:
                self.shopping(manage="delicacies")
            elif dice == 3:
                self.work()
            elif dice == 4:
                self.clean_home()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.cons = brand_list[self.brand]['cons']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.cons:
            self.fuel -= self.cons
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = { "Java developer": {"salary":50, "gladness_less": 10 },
             "Python developer": {"salary":40, "gladness_less": 3 },
             "C++ developer": {"salary":45, "gladness_less": 25 },
             "Rust developer": {"salary":70, "gladness_less": 1 },}

brand_of_car = {"BMW" : {"fuel" : 100, "strength" : 100, "cons" : 12},
                "Lada" : {"fuel" : 100, "strength" : 20, "cons" : 10},
                "Volvo" : {"fuel" : 80, "strength" : 120, "cons" : 8},
                "Ferrari" : {"fuel" : 60, "strength" : 80, "cons" : 14}}

human = Human("Vova")
for i in range(1, 366):
    if human.live(i) == False:
        break