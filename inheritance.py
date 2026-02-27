#single inheritance

class Animals:
    def __init__ (self,a):
        self.name=a

    def info(self):
        print("Animal name: ",self.name)

class Dog(Animals):
    def set_breed(self,b):
        self.breed=b

    def displaybreed(self):
        print("Breed : ", self.breed)

    def sound(self):
        print(self.name , "Bark")

dg=Dog("Buddy")
dg.set_breed("Lab")
dg.displaybreed()
dg.info()
dg.sound()


#single inheritance 2

class Person:
    def __init__ (self,a):
        self.name=a

    def show(self):
        print("Name: ",self.name)

class Student(Person):
    def display(self):
        print("student name: ",self.name)

s1=Student("Aswin")
s1.show()
s1.display()