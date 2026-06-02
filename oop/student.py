class Student:  # class variables : They define outside class

            Class_year = 2024
            number_of_students = 0

            def __init__(self,name,age):
                    self.name = name
                    self.age = age
                    Student.number_of_students += 1

student1 = Student("Ahmad",39)
student2 = Student("Ali",20)
student3 = Student("Hassan",20)
student4 = Student("Farhan",20)


print(student2.age)
print(student2.name)
print(Student.Class_year) # it is good practise that it is class variable and direcly accesing without class we cant tell which class it is

print(f"Student class Year is {Student.Class_year} and Number of Students are {Student.number_of_students}")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)