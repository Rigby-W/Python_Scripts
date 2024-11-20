password=input("What is the password? ")
if password.upper()=="PPAM".upper(): 
    print("Welcome to the adding machine!")
    x=input("What is the first number? ") 
    y=input("What is the second number? ")
    x=int (x)
    y=int (y)
    print(x+y)