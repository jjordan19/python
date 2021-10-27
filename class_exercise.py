class xyz():

    x = 1
    y = 2
    z = 3
p = xyz()

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
name = input("Enter your name: ")
age = input("enter your age: ")

human = Person(name, age)

print(f"Hi {human.name}, you're {human.age} years old.")
