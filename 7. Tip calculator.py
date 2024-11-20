print("Welcome to the tip calculator!")
x=input("What was the cost of the items? ") 
y=input("What is tip rate percent? ")
x=float (x)
y=float (y)
z=(x+(x*(y/100)))
z=str(z)
print(f"your total is: ${z}")

