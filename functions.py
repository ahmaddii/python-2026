def happy_birthday(name,age):
            print(f"Happy birthday to {name} !")
            print(f"Your age is : {age} !")
            print()


happy_birthday("Bro",20)
happy_birthday("ahmad",30)
happy_birthday("steve",40)

def display_invoice(userName, amount, due_date):
        print(f"Hello {userName}")
        print(f"Your bill is {amount} is due on {due_date}")


display_invoice("BroCode",45000,"01/02")

# now come to return used to end a function and send a result back to caller

def add(x,y):
        z = x+y
        return z

def sub(x,y):
        z = x-y
        return z

def mul(x,y):
        z = x*y
        return z

def divide(x,y):
        z = x/y
        return z

print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(divide(1,2))

def create_name(first_name,last_name):
        
        return f"{first_name.upper()} {last_name.upper()}"

print(create_name("ahmad","rasheed"))
print(create_name("fahad","khan"))