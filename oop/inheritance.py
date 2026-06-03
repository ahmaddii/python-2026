class Animal:  # inheritance

            def __init__(self,name):
                    self.name = name
                    self.is_alive = True

            def eat(Self):
                    print(f"{Self.name} is eating ")
            
            def sleep(self):
                    print(f"{self.name} is sleeping ")


class Dog(Animal):
        
        def speak(self):
                print("WOOF")


class Cat(Animal):
        
        def speak(self):
                print("MEOW")
         
        

class Mouse(Animal):
        
        def speak(self):
                print("Bahh")
        


dog = Dog("Puppy")
cat = Cat("Catty")
mouse = Mouse("mousey")

dog.speak()

print(dog.name)
print(dog.is_alive)
dog.sleep()