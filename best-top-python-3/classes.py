class Cars:

    def car(self):
        print("car")

    def json(self):
        return {'text':'text'}


cars = Cars().car()

print(Cars().json())