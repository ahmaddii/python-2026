# Weight Converter Prgram

weight = int(input("Weight: ")) # now weight store as an int

weightType = input("(K)g or (L)bs: ")

if weightType == "K" or weightType == "k":
            
            kg = round(weight/2.2)
            print(f"Weight in Kg : {kg}")

elif weightType == "L" or weightType == "l":
        
        pound = round(weight * 2.2)
        print(f"Weight in Pounds {pound} ") 

else:
        print("Plz Give Valid Input--")