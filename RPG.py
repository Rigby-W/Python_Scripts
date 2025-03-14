import time
name=input("What is your name? ")
gender=input("What is your gender? Male Female Or Other? ")
if gender.upper()=="Male".upper():
    pronoun1=("he")
    pronoun2=("him")
    pronoun3=("his")
    pronoun4=("sir")
    pronoun5=("mister")
if gender.upper()=="Female".upper():
    pronoun1=("she")
    pronoun2=("her")
    pronoun3=("hers")
    pronoun4=("madam")
    pronoun5=("miss")
if gender.upper()=="Other".upper():
    pronoun1=("they")
    pronoun2=("them")
    pronoun3=("theirs")
    pronoun4=("lord")
    pronoun5=("mix")
name=name.capitalize()
gold=0
print(f"Welcome {pronoun4} {name} to the wonderful world of Adventuria.")
time.sleep(1)
print(f"You wake up in a field dazed with only the memory of your name, {name}.")
print("-------------------------")
print("a town")
print("a forest")
print("-------------------------")
start=input("What do you see? ")
if start.upper()=="a town".upper():
    print(f"You see a town in the distance and you start walking towards the town and you find some money on the floor")
    loot=5
    gold+=loot
    time.sleep(0.75)
    print(f"You collected {loot} gold, you have {gold} gold!")
    in_town=True
    house=0
    while in_town==True:    
        print("-------------------------")
        print("a store")
        print("a house")
        print("a pub")
        print("-------------------------")
        town_location=input("Where do you wish to go? ")
        time.sleep(0.75)
        if town_location.upper()=="a store".upper() and gold>=4:
            print(f"You walk into the store and pick up some groceries for 4 gold, you have {gold-4} gold!")
            gold-=4
            time.sleep(0.5)
        if town_location.upper()=="a store".upper() and gold<4:
            print("You walk into the store but sadly you do not have enough money so you leave ")
            time.sleep(0.5)
        if town_location.upper()=="a house".upper() and house!=1:
            print("You walk into an old abandoned house and decide to stay there for the night and find a few pieces of gold")
            loot=7
            gold+=loot
            print(f"You collected {loot} gold, you have {gold} gold!")
            house=1
            time.sleep(0.75)
        if town_location.upper()=="a house".upper() and house==1:
            print("You walk into your house and rest for a bit")
            time.sleep(1.5)
        if town_location.upper()=="a pub".upper():
            print("You walk into a pub and meet the bartender, Henry")
            print(f"Henry- 'Oh hello there {pronoun5} {name}'")
            Drink_choice=input("Would you like something to drink its on the house? ")
            if Drink_choice.upper=="Y".upper() or "Yes".upper():
                print("You take a drink")
            if Drink_choice.upper=="n".upper() or "no".upper():
                print("You decline his offer to take a drink and leave")
if start.upper()=="a forest".upper():
    print("You walk into the forest")