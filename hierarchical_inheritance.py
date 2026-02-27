class Animal:
    def __init__(self):
        print("animal makes a sound")

class Cat(Animal):
    def __init__(self):
       
        print("cat meows")

class Dog(Animal):
    def dog(self):
        print("dog barks")

class Birds(Animal):
    def parrot(self):
        print("birds ki ki")


d = Cat()
c = Dog()
e = Birds()


c.dog()
e.parrot()