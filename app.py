age = 15
price = 19.45
first_name = input("What is your first name? ")
last_name =  input("What is your last name? ")
is_Online = True

birth_year = input("Enter your birth year ")

#converting the string to int

age1 = 2020 - int(birth_year) # now it returns the numeric not 


#float(),bool(),int(),str()

print(age1)
#string concatetation

print("Hello" + first_name)

#f string method
print(f"Hello my first name is {first_name} and last name is {last_name} : {is_Online} and my age is {age} ")


# 1st assigmnent

num1 = input("Enter the First Number = ") # num1 ko as a string lega
num2 = input("Enter the 2nd Number = ") # num2 ko as a string lega so we need type conversion for both

sum = num1 + num2

print(sum)

