print("Welcome to The Adventure of you!!")
name=input("What is your name? ")
print("You wake up in a tavern What do you choose to do?")
print("check")
print("leave")
print("drink")
start=input("what do you choose to do? ")
if start.upper()=="check".upper():
    print("You check the tavern and find a gold coin which you put in your pocket")
    print("leave")
    print("drink")
    action1=input("what do you choose to do? ")
    if action1.upper()=="leave".upper():
        print("you see a sign with 3 different places")
        print("Forest")
        print("Town")
        print("Den")
        location=input("where do you go? ")
        if location.upper()=="Den".upper():
            print("you walk into the dragons den")
            print("You died because the dragon caught you")
            print("Game over!")
            exit
        if location.upper()=="Forest".upper():
            print("You went out into the forest never to be seen again")
            print("Game over!")
            exit
        if location.upper()=="Town".upper():
            print("You walk into town and a salesman asks you if you want to try some magic bread?")
            answer=input("[Y/N]? ")
            if answer.upper()=="N".upper():
                print("you refuse his offer and go home safely")
                print("The end")
                exit
            if answer.upper()=="Y".upper():
                print("You purchase a piece of bread and sadly it turns out it was poisonous...")
                print("Game over!")
                exit
    if action1.upper()=="drink".upper():
        print("You ask the bartender for a drink")
        print("the bartender gives you a drink and then he allows you to sleep in the tavern")
        print("The end")
        exit    
if start.upper()=="leave".upper():
    print("you see a sign with 3 different places")
    print("Forest")
    print("Town")
    print("Den")
    location=input("where do you go? ")
    if location.upper()=="Den".upper():
        print("you walk into the dragons den")
        print("You died because the dragon caught you")
        print("Game over!")
        exit
    if location.upper()=="Forest".upper():
        print("You went out into the forest never to be seen again")
        print("Game over!")
        exit
    if location.upper()=="Town".upper():
        print("You walk into town and a salesman asks you if you want to try some magic bread?")
        answer=input("[Y/N]? ")
        if answer.upper()=="N".upper():
            print("you refuse his offer and go home safely")
            print("The end")
            exit
        if answer.upper()=="Y".upper():
            print("you cannot purchase a peice and so you refuse his offer and go home safely")
            print("The end")
            exit
if start.upper()=="drink".upper():
    print("You ask the bartender for a drink")
    print("the bartender tells you that you dont have enough money for a drink but he still allows you to sleep in the tavern")
    print("The end")
    exit