class Car:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def getCar(self):
        print("Your car is: "+ self.name + " And his type is: " + self.type)