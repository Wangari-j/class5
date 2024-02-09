class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is" + self)

p1 = Person("John",40)
p1.myFunc