# duck type using polymorphism


class Animal:

            alive = True

class Dog(Animal):
        
        def speak(self):
                print("Woof")

class Cat(Animal):
        
        def speak(self):
                print("MEOW")

class Car:
        
        alive = False
        
        def speak(Self):
                print("HUNK")


animals = [Dog(),Cat(),Car()]


for animal in animals:
        animal.speak()
        print(animal.alive)