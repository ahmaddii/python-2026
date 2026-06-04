# abstract class

from abc import ABC,abstractmethod


class vechile(ABC):
            
            @abstractmethod

# we dont define them we define them in children class
            def go(self):
                    pass

            @abstractmethod

            def stop(self):
                    pass


class Car(vechile):
        
        def go(self):
                print("You drive the car")

        def stop(self):
                print("You drive the car")


car = Car()
car.go()
car.stop()


class MotorCycle(vechile):
        
        def go(self):
                print("You drive the motor bike")

        def stop(self):
                print("You stop the motor bike")

motor = MotorCycle()
motor.go()

class boat(vechile):
        
         def go(self):
                print("You drive the boat ")
         
         def stop(self):
                print("You stop the boat ")


        

boat1 = boat()

boat1.go()
