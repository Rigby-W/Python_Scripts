number=input("Enter a number: ")
number=int(number)
x=range(number)
for val in x:
    check1=val%5
    check2=val%3
    if check1==0 or check2==0:
        number += val 
print(number)