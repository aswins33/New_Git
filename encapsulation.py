class Person:
    def __init__(self, name, age):
        self.name = name     
        self.age = age        

    def greet(self):
        print(f"Hi, I'm {self.name}")

p = Person("Aswin", 23)
print(p.name)    
p.greet()        