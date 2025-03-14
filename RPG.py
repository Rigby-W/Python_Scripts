import time
name = input("What is your name? ").capitalize().strip()
gender = input("What is your gender? Male, Female, Or Other? ").strip().lower()
def get_pronouns(gender):
    pronouns = {
        "MALE": ("he", "him", "his", "sir", "mister"),
        "FEMALE": ("she", "her", "hers", "madam", "miss"),
        "OTHER": ("they", "them", "theirs", "lord", "mix")
    }
    return pronouns.get(gender.upper(), ("they", "them", "theirs", "lord", "mix"))
(pronoun1, pronoun2, pronoun3, pronoun4, pronoun5) = get_pronouns(gender)
def town_adventure(gold, pronoun1, pronoun2, pronoun3, pronoun4, pronoun5, name):
    print(f"You see a town in the distance and you start walking towards the town and you find some money on the floor")
    loot = 5
    gold += loot
    time.sleep(0.75)
    print(f"You collected {loot} gold, you have {gold} gold!")
    in_town = True
    house = 0
    while in_town:
        print("-------------------------")
        print("a store")
        print("a house")
        print("a pub")
        print("leave town")
        print("-------------------------")
        town_location = input("Where do you wish to go? ").strip().lower()
        time.sleep(0.75)

        if town_location == "a store":
            if gold >= 4:
                print(f"You walk into the store and pick up some groceries for 4 gold, you have {gold-4} gold!")
                gold -= 4
            else:
                print("You walk into the store but sadly you do not have enough money so you leave ")
        elif town_location == "a house":
            if house != 1:
                print("You walk into an old abandoned house and decide to stay there for the night and find a few pieces of gold")
                loot = 7
                gold += loot
                print(f"You collected {loot} gold, you have {gold} gold!")
                house = 1
            else:
                print("You walk into your house and rest for a bit")
        elif town_location == "a pub":
            print("You walk into a pub and meet the bartender, Henry")
            print(f"Henry- 'Oh hello there {pronoun5} {name}'")
            drink_choice = input("Would you like something to drink its on the house? ").strip().lower()
            if drink_choice in ("y", "yes"):
                print("You take a drink")
            elif drink_choice in ("n", "no"):
                print("You decline his offer to take a drink and leave")
        elif town_location == "leave town":
            in_town=False
        else:
            print("Invalid choice, please choose again.")
        time.sleep(0.5)
def forest_adventure(gold, pronoun1, pronoun2, pronoun3, pronoun4, pronoun5, name):
    print(f"you walk into a deep forest and stumble a shack in the woods with an old man inside")

def main(): 
    time.sleep(1)
    print("-------------------------")
    print("a town")
    print("a forest")
    print("-------------------------")
    start = input("Where do you wish to go? ").strip().lower()
    if start == "a town":
        town_adventure(gold, pronoun1, pronoun2, pronoun3, pronoun4, pronoun5, name)
    elif start == "a forest":
        forest_adventure(gold, pronoun1, pronoun2, pronoun3, pronoun4, pronoun5, name)
    else:
        print("Invalid choice, please choose a valid option.")
gold = 0
print(f"Welcome {pronoun4} {name} to the wonderful world of Adventuria.")
time.sleep(1)
print(f"You wake up in a field dazed with only the memory of your name, {name}.")
while True:
    main()
