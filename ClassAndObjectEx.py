
# class and object example

# __init__ is constructor method
# self refers the current object instance = this in java
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name}")

person1= Person("alice", 20)
person1.greet()


