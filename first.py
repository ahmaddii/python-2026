# 1st assigmnent

num1 = input("Enter the First Number = ") # num1 ko as a string lega
num2 = input("Enter the 2nd Number = ") # num2 ko as a string lega so we need type conversion for both

#sum = num1 + num2 # with this we get 1 or 2 becuase it concatenate two strings

sum = float(num1) + float(num2)
sub = float(num1) - float(num2)
mul = float(num1) * float(num2)
divide = float(num1) / float(num2)
module = float(num1) % float(num2)

print(sum)
print(sub)
print(mul)
print(divide)
print(module)


