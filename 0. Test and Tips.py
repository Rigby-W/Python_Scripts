# math commands:
# x<=y is x is less than or equal to y
# x>=y is x is greater than or equal to y
# x==y is x is equal to y
# x<y is x is less than y
# x>y is x is greater than y
# x%y is to find the remainder
# x**y is x to the power of y
# useful terminal commands: 
# "python": runs the python command with the same starting digit
# "clear" : clears the termial to make it look cleaner
# "echo" : echoes text into the terminal
# Variable types: 
# int=integer (number only)
# str=string (words and numbers allowed but cant be used for math) 
# float= a floating integer (useful for precise calculations)
# github commands:
# git add (file name)
# git commit -m "(share comment on changelog)"
# git push -u origin main
# git pull --all
from datetime import datetime
import time
import random
from random import randint
print("this is a testing file, code here may or may not work so proceed with caution")
name=input("What is your name? ")
password=input("Enter Password to continue: ")
if password.upper()=="RigbyW".upper(): 
    print(f"Password Accepted. Welcome into the testing file, {name}.")
    while True:        
        print("-------------")
        print("Current files")
        print("-------------")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        print("tip")
        print("root")
        print("square")
        print("clock")
        print("dice")
        print("military")
        print("guess")
        print("hint")
        print("-------------")        
        filetype=input("which testing file do you wish to access? ")
        if filetype.upper()=="add".upper():
            print("Welcome to the adding machine!")
            first_number=input("What is the first number? ") 
            second_number=input("What is the second number? ")
            first_number=float (first_number)
            second_number=float (second_number)
            print(first_number+second_number)
        elif filetype.upper()=="subtract".upper():
            print("Welcome to the subtracting machine!")
            first_number=input("What is the first number? ") 
            second_number=input("What is the second number? ")
            first_number=float (first_number)
            second_number=float (second_number)
            print(first_number-second_number)
        elif filetype.upper()=="multiply".upper():
            print("Welcome to the multiplying machine!")
            first_number=input("What is the first number? ") 
            second_number=input("What is the second number? ")
            first_number=float (first_number)
            second_number=float (second_number)
            print(first_number*second_number)
        elif filetype.upper()=="divide".upper():
            print("Welcome to the dividing machine!")
            first_number=input("What is the first number? ") 
            second_number=input("What is the second number? ")
            first_number=float (first_number)
            second_number=float (second_number)
            print(first_number/second_number)
        elif filetype.upper()=="tip".upper():
            print("Welcome to the tip calculator! With new rounding technology!")
            basecost=input("What was the cost of the items? ") 
            tiprate=input("What is tip rate percent? ")
            basecost=float (basecost)
            tiprate=float (tiprate)
            total=(basecost+(basecost*(tiprate/100)))
            total= round(total, 2)
            total=str(total)
            print(f"Your total is: ${total}")
        elif filetype.upper()=="root".upper():
            print("Welcome to the square rooting machine")
            first_number=input("what number do you wish to square root? ")
            first_number=float (first_number)
            print(first_number ** 0.5)
        elif filetype.upper()=="square".upper():
            print("Welcome to the squaring machine")
            first_number=input("what number do you wish to square? ")
            first_number=float (first_number)
            print(first_number ** 2)
        elif filetype.upper()=="clock".upper():
            now = datetime.now() 
            dt_string = now.strftime("%d/%m/%Y %H:%M")
            print("The date and time is:", dt_string)
        elif filetype.upper()=="dice".upper():
            number=input("What is the dice that you wish to roll: a d")
            dice=input("How many times should your dice roll: ")
            dice= int(dice)
            number= int(number)
            x=0
            for i in range (dice):    
                Roll=(random.randrange(1, number, 1))
                print(f"you rolled a {Roll}")
                time.sleep (0.3)
                x+=Roll
            print(f"Your total is {x}")
        elif filetype.upper()=="military".upper():
            print("Welcome to the civilian to military time converter")
            hour=input("what is the hour? ")
            minute=input("what is the minute? ")
            minute=int(minute)
            hour=int(hour)
            am_or_pm=input("Is it am or pm? ")
            if am_or_pm.upper()=="pm".upper()and minute<10: 
                pm_hour=(hour+12)
                print(f"The time is {pm_hour}:0{minute}!")
            elif am_or_pm.upper()=="am".upper()and minute<10:
                print(f"The time is {hour}:0{minute}!")
            elif am_or_pm.upper()=="pm".upper()and minute>=10: 
                pm_hour=(hour+12)
                print(f"The time is {pm_hour}:{minute}!")
            elif am_or_pm.upper()=="am".upper()and minute>=10:
                print(f"The time is {hour}:{minute}!")
        elif filetype.upper()=="guess".upper():
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
        elif filetype.upper()=="hint".upper():
            filehint=input("what file do you wish to learn about? ")
            if filehint.upper()=="add".upper():
                print("adds two numbers together")
            elif filehint.upper()=="subtract".upper():
                print("subtracts the second number from the first number")
            elif filehint.upper()=="multiply".upper():
                print("multiplies two numbers together")
            elif filehint.upper()=="divide".upper():
                print("Divides the first number by the second number")
            elif filehint.upper()=="tip".upper():
                print("Calculates a tip using the price of an item and the current tip rate")
            elif filehint.upper()=="root".upper():
                print("Square roots a number")
            elif filehint.upper()=="square".upper():
                print("Squares a number")
            elif filehint.upper()=="clock".upper():
                print("Displays the time")
            elif filehint.upper()=="dice".upper():
                print("Rolls a dice with any number of sides")
            elif filehint.upper()=="military".upper():
                print("Changes the inputed time to military time")
            elif filehint.upper()=="guess".upper():
                print("Opens a guessing game where you have to guess a number 1-100")
            elif filehint.upper()=="hint".upper():
                print("displays what a file does in cae you do not know what it does")
        retry=input("do you wish to access a new file? [y/n] ")
        if retry.upper()=="n".upper():
            break