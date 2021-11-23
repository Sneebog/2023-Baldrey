#plinkle
class  Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0
        print("A new dog is born :)")
    def bark(self):
        for i in range(20):
            print("feed me father")
mydog1 = Dog()
mydog1.age = 10
mydog1.name = "drake"
mydog1.weight = 24
class Cat():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0
        print("you feel a shiver through your spine")
    def prick(self):
        for i in range(10):
            print("Hi I am " + self.name)
myCat = Cat()
myCat.age = 10
myCat.name = "plimbus"
myCat.weight = 24
myCat.prick()