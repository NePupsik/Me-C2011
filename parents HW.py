class Grandparents:
    def __init__(self):
        self.age = 70
        self.high = 140
        self.whoheis = "Human"
        print(self.age)
        print(self.high)
        print(self.whoheis)

class parents(Grandparents):
    def __init__(self):
        self.age = 35
        print(self.age)
        print(self.high)
        print(self.whoheis)
class children(parents):
    def __init__(self):
        self.age = 10
        print(self.age)
        print(self.high)
        print(self.whoheis)

class babies(children):
    def __init__(self):
        self.age = 4
        self.high = 65
        print(self.age)
        print(self.high)
        print(self.whoheis)