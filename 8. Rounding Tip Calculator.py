print("Welcome to the tip calculator! With new rounding technology!")
x=input("What was the cost of the items? ") 
y=input("What is tip rate percent? ")
x=float (x)
y=float (y)
z=(x+(x*(y/100)))
z= round(z, 2)
z=str(z)
print(f"Your total is: ${z}")