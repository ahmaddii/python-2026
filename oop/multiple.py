
# MULTIPLE Inheritance 

class Animal:
        
        def __init__(self,name):
                
                self.name = name
                

        def eat(self):
                print("This animal eats")

class Prey(Animal):
            def flee(self):
                    print(f"The  {self.name} is Fleeing")

class Predator(Animal):
            
            def hunt(self):
                    print("The animal is Hunting")

class Rabbit(Prey):
        pass
            

class Hawk(Predator):
            pass

class Fish(Prey,Predator):
        pass


rabbit = Rabbit("Baba")
rabbit.flee()

fish = Fish("Nemo")

fish.hunt()
fish.eat()