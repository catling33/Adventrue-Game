import time
import random
import functools
print = functools.partial(print, flush=True)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            break
    return response


def print_pause(words):
    print(words)
    time.sleep(1)


def intro(items, name, enemies, weapons, blood):
    print_pause("Hi, welcome to the Wonder Land.")
    print_pause("I am Alice.")
    name.append(input("What's your name?\n"))
    time.sleep(1)
    print_pause("OK! " + name[0] + ", Good luck!\n")
    print_pause("Please keep in mind, you only have 5 blood.")
    print_pause("If you lost all of the blood. You will die.\n")
    print_pause("Now you see a very dangerous open field.")
    print_pause("In front of you are three passageways.\n")


def field(items, name, enemies, weapons, blood):
    print_pause("Enter 1 to go into the house.\n"
                "Enter 2 to peer into the cave.\n"
                "Enter 3 to jump into the lake.\n")
    print("What would you like to do?")
    response = valid_input("(Please enter 1, 2 or 3)\n", ["1", "2", "3"])
    if response == "1":
        house(items, name, enemies, weapons, blood)
    elif response == "2":
        cave(items, name, enemies, weapons, blood)
    elif response == "3":
        lake(items, name, enemies, weapons, blood)


def house(items, name, enemies, weapons, blood):
    enemy = random.choice(enemies)
    print_pause("\nYou approached the door of the house.")
    print_pause(f"There is a {enemy} in the house.")
    print_pause(f"The {enemy} attacks you!\n")
    attack = valid_input("Do you wanna 1)attack or 2)run away?\n", ["1", "2"])
    if attack == "1":
        if "a dagger" in items:
            print_pause(f"You killed the {enemy}")
            if "a golden necklace" in items:
                print_pause(f"You rubbed the golden necklace on {enemy}.")
                print_pause("You went back home safely and enjoyed the rest of"
                            " your life!\n")
                play_again(name)
            else:
                print_pause("However, you didn't have enough money to go back"
                            " home.")
                print_pause("You called your parents and cried.\n")
                play_again(name)
        elif "a sword" in items:
            battle_weak(items, name, enemies, weapons, blood)
        else:
            battle_strong(items, name, enemies, weapons, blood)

    elif attack == "2":
        print_pause("You ran back to the field like crazy.")
        print_pause(f"The {enemy} didn't catch you.\n")
        field(items, name, enemies, weapons, blood)


def cave(items, name, enemies, weapons, blood):
    weapon = random.choice(weapons)
    print_pause("You peered into the cave.")
    if weapon in items:
        print_pause("Opps, nothing.")
        print_pause("You went back to the field.\n")
        field(items, name, enemies, weapons, blood)
    else:
        print_pause(f"You picked up {weapon}!")
        items.append(weapon)
        print_pause("You went back to the field.\n")
        field(items, name, enemies, weapons, blood)


def lake(items, name, enemies, weapons, blood):
    print_pause("You jumped into the lake.")
    print_pause("The Koi King woke up and asked you for food.")
    if "a carrot cake" in items:
        print_pause("You gave him the carrot cake.")
        if "a dagger" in items:
            print_pause("The Koi King said he is sick of carrot cake.")
            print_pause("He ate you...\n")
            play_again(name)
        else:
            print_pause("The Koi King really liked you and gave you a crystal"
                        " dagger!")
            items.append("a dagger")
            print_pause("You happily went back to the field.\n")
            field(items, name, enemies, weapons, blood)
    else:
        print_pause("You didn't have anything to eat.")
        if len(items) != 0:
            lose = random.choice(items)
            items.remove(lose)
            print_pause(f"He took away {lose} from you and let you go.")
            print_pause("You quickly ran back to the field.\n")
            field(items, name, enemies, weapons, blood)
        else:
            print_pause("He was very angry and chased you away...")
            print_pause("You went back to the field.\n")
            field(items, name, enemies, weapons, blood)


def battle_strong(items, name, enemies, weapons, blood):
    blood_lost = random.randint(0, 3)
    blood -= blood_lost
    print_pause("You lost " + str(blood_lost) + " blood.")
    battle_result(items, name, enemies, weapons, blood)


def battle_weak(items, name, enemies, weapons, blood):
    blood_lost = 1
    blood -= blood_lost
    print_pause("You lost " + str(blood_lost) + " blood.")
    battle_result(items, name, enemies, weapons, blood)


def battle_result(items, name, enemies, weapons, blood):
    if blood <= 0:
        print_pause("You lost all your blood...You lose.\n")
        play_again(name)
    elif blood > 0:
        print_pause("You have " + str(blood) + " blood remaining.")
        print_pause("You quickly ran back to the field...\n")
        field(items, name, enemies, weapons, blood)


def play_game():
    blood = 5
    items = []
    name = []
    enemies = ["BIG CAT", "JOKER", "BLUE BUBBLE", "FAKE SMILE"]
    weapons = ["a golden necklace", "a carrot cake", "a dagger", "a sword"]
    intro(items, name, enemies, weapons, blood)
    field(items, name, enemies, weapons, blood)


def play_again(name):
    again = valid_input("Would you like to play again? y or n\n", ["y", "n"])
    if "y" in again:
        play_game()
    elif "n" in again:
        print_pause("Bye! " + name[0] + "!")


play_game()
