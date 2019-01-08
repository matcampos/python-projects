
class Person:

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def getPerson(self):
        print("This person name is:" + self.name + " and his job is: " + self.job)