course = "Python for begineers"

print(course.upper())
print(course)

print(course.find("y"))

print("for" in course) # it gives true 

print(course.replace("for","r"))

# so these methods actually create a new strings rather then changing the original e.g

print(course) # see it remains original so by default they are immutable
