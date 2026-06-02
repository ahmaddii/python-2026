from car import Car


car1 = Car("Mustang",2026,"Red",False)
car2 = Car("Ford",2024,"blue",True)

car2.stop()
car1.drive()
car2.describe()

print(car1.model)
print(car1.color)
print(car1.year)

print(car2.model)