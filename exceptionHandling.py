# exception : an event that interuupts the flow of program (zeroDivisionError,TypeError
# ValueError)
#
#1/0
#1+ "1"

#int("Pizza")
# we handle all of these exception using try except finally:

try:
            number = int(input("Enter a number "))
            print(1/number)

except ZeroDivisionError:
        print("You cant divide a number by zero")

except ValueError:
        print("Enter Only Number plz ")

except Exception:
        print("Something Went Wrong")
# finally block alwasys execute no matter exception happend or not
finally:
        print("Do Some CleanUp here")

# except Exception if we do this it will catch all excpetion and show something went wrong its a bad practise we want to tell user what went wrong

 # so if user type 0