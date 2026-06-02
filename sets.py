# e.g you have list of items and if you want to remove the duplicates from them

#numbers  = [1,2,3,3,4]

#uniques = set(numbers)

#print(uniques)

# how we define sets using curly braces

#second = {1,2,5}

#print(second)

#second.add(6)
#second.remove(1)

#print(second)

# e.g we have 2 sets

numbers = [1,1,2,3,4]
first = set(numbers)

second = {1,4,5}

print(first | second) # union of the two sets are another set

print(first & second) # this will take intersection common one from both

print(first - second)

# sets are Unordered thats why we cant acces thorugh index with sets we use rarley

if 1 in first:
            print("Yes")