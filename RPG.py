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
    pronoun4=("mix")
    pronoun5=("lord")
name=name.capitalize()
gold=0
print(f"Welcome {pronoun5} {name} to the wonderful world of Adventuria.")
print(f"You wake up in a field dazed with only the memory of your name, {name}.")
print("-------------------------")
print("a town")
print("a forest")
print("-------------------------")
choice1=input("What do you see? ")
if choice1.upper()=="a town".upper():
    print(f"You see a town in the distance and you start walking towards the town and you find some money on the floor")
    loot=5
    gold+=loot
    print(f"You collected {loot} gold, you have {gold} gold!")
    print("-------------------------")
    print("a store")
    print("a house")
    print("a pub")
    print("-------------------------")
if choice1.upper()=="a forest".upper():
    print("You walk into the forest")