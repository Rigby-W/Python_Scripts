from datetime import datetime
import time
import random
print("This is a testing file, code here may or may not work so proceed with caution")
name=input("What is your name? ")
password=input("Enter Password to continue: ")
if password.upper()=="password".upper(): 
    print(f"Password Accepted. Welcome into the testing file, {name}.")
    while True:
        print("-------------")
        print("Current files")
        print("-------------")
        print("Calculator")
        print("Tip")
        print("Clock")
        print("Dice")
        print("Games")
        print("Tarot")
        print("Hint")
        print("-------------")        
        filetype=input("Which testing file do you wish to access? ")
        if filetype.upper()=="calculator".upper():
            print("Welcome to the calculator!")
            first_number=input("What is the first number? ") 
            second_number=input("What is the second number? ")
            first_number=float (first_number)
            second_number=float (second_number)
            print("Current calculator programs")
            print("---------------------------")
            print("add")
            print("subtract")
            print("multiply")
            print("divide")
            print("exponent")
            print("remainder")
            print("---------------------------")
            calculate=input("What would you like to do between these two numbers? ")    
            if calculate.upper()=="add".upper():
                print(first_number+second_number)
            if calculate.upper()=="subtract".upper():
                print(first_number-second_number)
            if calculate.upper()=="divide".upper():
                print(first_number/second_number)
            if calculate.upper()=="multiply".upper():
                print(first_number*second_number)
            if calculate.upper()=="exponent".upper():
                print(first_number**second_number)
            if calculate.upper()=="remainder".upper():
                print(first_number%second_number)
        elif filetype.upper()=="tip".upper():
            print("Welcome to the tipping machine!")
            basecost=input("What was the cost of the purchase? ") 
            tiprate=input("What is tip rate in percent? ___%")
            basecost=float (basecost)
            tiprate=float (tiprate)
            total=(basecost+(basecost*(tiprate/100)))
            total= round(total, 2)
            total=str(total)
            print(f"Your total is: ${total}")
        elif filetype.upper()=="clock".upper():
            now = datetime.now() 
            dt_string = now.strftime(f"%m/%d/%Y %H:%M")
            print(f"The date and time is: {dt_string}")
        elif filetype.upper()=="dice".upper():
            number=input("What is the dice that you wish to roll: a d")
            dice=input("How many times should your dice roll: ")
            dice= int(dice)
            number= int(number)
            number+=1
            x=0
            for i in range (dice):    
                Roll=(random.randrange(1, number, 1))
                print(f"you rolled a {Roll}")
                time.sleep (0.3)
                x+=Roll
            print(f"Your total is {x} and your average roll was {x/dice}")
        elif filetype.upper()=="Games".upper():
            print("Current games")
            print("-------------------------")
            print("Guessing Game (or GG)")
            print("Rock Paper Scissors (or RPS)")
            print("-------------------------")
            gametype=input("What game would you like to play? ")
            if gametype.upper()=="guessing game".upper() or gametype.upper()=="GG".upper():
                value=random.randint(1,100)
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
                    if x==10:
                        print("You lose :(")
            elif gametype.upper()=="rock paper scissors".upper() or gametype.upper()=="rps".upper():
                while True:
                    choice=input("rock paper or scissors? (Or R, P, S) ")
                    if choice.upper()=="rock".upper() or choice.upper()=="r".upper():
                        rps=(random.randrange(1, 4, 1))
                        if rps==1:
                            print("your opponent chose rock you tie")
                        elif rps==2:
                            print("your opponent chose paper you lose")
                            break
                        elif rps==3:
                            print("your opponent chose scissors you win")
                            break
                    elif choice.upper()=="paper".upper() or choice.upper()=="p".upper():
                        rps=(random.randrange(1, 4, 1))
                        if rps==1:
                            print("your opponent chose rock you win")
                            break
                        elif rps==2:
                            print("your opponent chose paper you tie")
                        elif rps==3:
                            print("your opponent chose scissors you lose")
                            break
                    elif choice.upper()=="scissors".upper() or choice.upper()=="s".upper():
                        rps=(random.randrange(1, 4, 1))
                        if rps==1:
                            print("your opponent chose rock you lose")
                            break
                        elif rps==2:
                            print("your opponent chose paper you win")
                            break
                        elif rps==3:
                            print("your opponent chose scissors you tie")
        elif filetype.upper()=="tarot".upper():
            Minor_Arcana =('Ace of Swords','Two of Swords','Three of Swords','Four of Swords','Five of Swords','Six of Swords','Seven of Swords','Eight of Swords','Nine of Swords','Ten of Swords','Page of Swords','Knight of Swords','Queen of Swords','King of Swords','Ace of Wands','Two of Wands','Three of Wands','Four of Wands','Five of Wands','Six of Wands','Seven of Wands','Eight of Wands','Nine of Wands','Ten of Wands','Page of Wands','Knight of Wands','Queen of Wands','King of Wands','Ace of Pentacles','Two of Pentacles','Three of Pentacles','Four of Pentacles','Five of Pentacles','Six of Pentacles','Seven of Pentacles','Eight of Pentacles','Nine of Pentacles','Ten of Pentacles','Page of Pentacles','Knight of Pentacles','Queen of Pentacles','King of Pentacles','Ace of Cups','Two of Cups','Three of Cups','Four of Cups','Five of Cups','Six of Cups','Seven of Cups','Eight of Cups','Nine of Cups','Ten of Cups','Page of Cups','Knight of Cups','Queen of Cups','King of Cups')
            Major_Arcana = ('The Magician','The High Priestess','The Empress','The Emperor','The Hierophant','The Lovers','The Chariot','Strength','The Hermit','Wheel of Fortune','Justice','The Hanged Man','Death','Temperance','The Devil','The Tower','The moon','The sun','Judgement','The World')
            All_Arcana = ('Ace of Swords','Two of Swords','Three of Swords','Four of Swords','Five of Swords','Six of Swords','Seven of Swords','Eight of Swords','Nine of Swords','Ten of Swords','Page of Swords','Knight of Swords','Queen of Swords','King of Swords','Ace of Wands','Two of Wands','Three of Wands','Four of Wands','Five of Wands','Six of Wands','Seven of Wands','Eight of Wands','Nine of Wands','Ten of Wands','Page of Wands','Knight of Wands','Queen of Wands','King of Wands','Ace of Pentacles','Two of Pentacles','Three of Pentacles','Four of Pentacles','Five of Pentacles','Six of Pentacles','Seven of Pentacles','Eight of Pentacles','Nine of Pentacles','Ten of Pentacles','Page of Pentacles','Knight of Pentacles','Queen of Pentacles','King of Pentacles','Ace of Cups','Two of Cups','Three of Cups','Four of Cups','Five of Cups','Six of Cups','Seven of Cups','Eight of Cups','Nine of Cups','Ten of Cups','Page of Cups','Knight of Cups','Queen of Cups','King of Cups','The Magician','The High Priestess','The Empress','The Emperor','The Hierophant','The Lovers','The Chariot','Strength','The Hermit','Wheel of Fortune','Justice','The Hanged Man','Death','Temperance','The Devil','The Tower','The moon','The sun','Judgement','The World')
            arcana=input("Would you like only Major, Minor, or All? ")
            reverse_test=(random.randrange(1, 3, 1))
            if reverse_test==1:
                if arcana.upper()=="major".upper():
                    print(f"Your card is {random.choice(Major_Arcana)} reversed")
                elif arcana.upper()=="minor".upper():
                    print(f"Your card is {random.choice(Minor_Arcana)} reversed")
                elif arcana.upper()=="All".upper():
                    print(f"Your card is {random.choice(All_Arcana)} reversed")
            elif reverse_test!=1:
                if arcana.upper()=="major".upper():
                    print(f"Your card is {random.choice(Major_Arcana)} upright")
                elif arcana.upper()=="minor".upper():
                    print(f"Your card is {random.choice(Minor_Arcana)} upright")
                elif arcana.upper()=="All".upper():
                    print(f"Your card is {random.choice(All_Arcana)} upright")
        elif filetype.upper()=="hint".upper():
            filehint=input("What file do you wish to learn about? ")
            if filehint.upper()=="calculator".upper():
                print("A rudimentary calculator")
            elif filehint.upper()=="tip".upper():
                print("Calculates a tip using the price of an item and the current tip rate")
            elif filehint.upper()=="clock".upper():
                print("Displays the time")
            elif filehint.upper()=="dice".upper():
                print("Rolls a dice with any number of sides any number of times")
            elif filehint.upper()=="games".upper():
                print("Opens a list of a few games you can play")
            elif filehint.upper()=="tarot".upper():
                print("Gives you a random tarot card")
            elif filehint.upper()=="hint".upper():
                print("Displays what a file does in case you do not know what it does")
        retry=input("Do you wish to access a new file? [y/n] ")
        if retry.upper()=="n".upper():
            break
