from Car import Car

# for self we dont pass the anything

try:
        car_1 = Car("Mercedes","Corvette",2011,"red")
        car_2 = Car("Ford","Mustang",2022,"blue")
        print(car_1.make)
        car_1.stop()
        car_2.drive()

except TypeError:
        print("Plz Pass the Argument Values")