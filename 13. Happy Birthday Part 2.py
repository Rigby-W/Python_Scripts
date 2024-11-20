z=input("What is your name? ")
x=input("Is today your birthday? ")
y=input("How old are you turning? ")
y=int(y)
if x=="Yes":
    if y==1:print(f"Happy Birthday {z} congrats on your {y}st birthday!!!")
    elif y==2:print(f"Happy Birthday {z} congrats on your {y}nd birthday!!!")
    elif y==3:print(f"Happy Birthday {z} congrats on your {y}rd birthday!!!")
    else: print(f"Happy Birthday {z} congrats on your {y}st birthday!!!")
