class Person:

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def print_name(self):
        print("My name is {}".format(self.name))

    def print_age(self):
        print(f'My age is {self.age}')

    def print_location(self):
        print("My age is {location}".format(location=self.location))
