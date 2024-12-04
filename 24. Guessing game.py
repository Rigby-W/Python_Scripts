from random import randint
value=randint(1,100)
x=0
for i in range(10):
    x+=1
    response=input("guess a number 1-100: ")
    response=int(response)

    if response==value:
        print("You win")
        break
    elif response > value:
        print(f"{response} is greater than the answer you have {10-x} guesses left")
    elif response < value:
        print(f"{response} is less than than the answer you have {10-x} guesses left")
