# Employe Managment system
import json

print("===Employee Managment System===")

user_input = int(input(" Plz Select from 1/4 for Employe Manament "))

emp_path = "/home/malikahmadrasheed/Downloads/emp.json"


def addEmployee():
    
    addEmp = {
        "name": input("Enter your name "),
        "age": int(input("Enter your age ")),
        "job": input("Enter you job ")
    }

    try:
        with open(emp_path, mode="w") as file:
            json.dump(addEmp, file, indent=4)

    except Exception as e:
        print("Error:", e)

def viewEmployee():
    