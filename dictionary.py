# a collection of {key:value} pairs ordered and changeable . no duplicates

capitals = {

            "USE": "Washington D.C",
            "India": "Delhi",
            "Pakistan": "Islamabad",
            "Russia":  "Moscow"
 
}

#print(dir(capitals))

# using get you can get any value with key

print(capitals.get("Pakistan"))

if capitals.get("Japan"):
            print("Capital Exists")

else:
        print("Capitals dosent exists")

# how to update dictionary

capitals.update({"Germanmy": "Berlin"})
print(capitals)

# if you want to remove the item in dic

capitals.pop("India")

print(capitals)

# and we have also pop item which removes the latest item  which we added

capitals.popitem()
print(capitals)

#keys = capitals.keys()

#print(keys)

for key in capitals.keys():
        print(key)

#for key,value in capitals.keys(),capitals.values():
 #       print(f"The key is : {key}, and the value is {value}")

items = capitals.items()
print(items)

# for getting every key value pair

for key,value in capitals.items():
        print(f"The key is {key} and the value is {value}")