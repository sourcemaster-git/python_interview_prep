from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.__name = name  # Encapsulation - private

    # getter
    @property
    def name(self):  # Encapsulation - Read Only
        return self.__name

    def describe(self):
        print(f"{self.name} says: {self.speak()}")

    @abstractmethod
    def speak(self): ...  # Abstract-contract


class Dog(Animal):  # Inheritance
    def speak(self):
        return "Woof!"  # Polymorphishm -- override


class Cat(Animal):  # Inheritance
    def speak(self):
        return "Meow!"  # Polymorphism -- override


for a in [Dog("Rex"), Cat("Luna")]:
    a.describe()
