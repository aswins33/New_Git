# Parent class
class Animal:
    def __init__(self):
        print("Animal constructor called")

# Child class 1
class Dog(Animal):
    def __init__(self):
        super().__init__ 
        print("Dog constructor called")

# Child class 2
class Cat(Animal):
    def __init__(self):
        super().__init__ 
        print("Cat constructor called")


d = Dog()
c = Cat()