names = ["Ahmad","Bob","Mosh"]

print(names[1])
print(names[-3])

names[0] = "Ali"

print(names)

print(names[0:2])

# List Methods

numbers = [1,2,3,4,5]

numbers.append(6) # for single insertion in the list

numbers.extend([7,8,9,10]) # for multiple insertion in list

numbers.insert(0,-1)

numbers.remove(3)

#numbers.clear()

print(1 in numbers) # check value exists or not

print(len(numbers)) # tells us length of our list

print(numbers)