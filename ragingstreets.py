import time
import random
import sys
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

enemies = ["Zamza", "Vehelits"]
def some_function():
    enemy = random.choice(enemies)
    print_pause(f"The enemy {enemy} ......")
    if enemy == "Zamza":
        print_pause(f"Zamza is very powerful, but luckily you are equiped to deal "
                    "with his barage of attacks.  You not only see him, your Broadsword "
                    "is powerful enough to defeat him")
    elif enemy == "Vehelits":
        print_pause(f" Vehelits is very strong, with incredible reach. "
                    "your broadsword outreaches his every move. ")


def start():
    print_pause("Welcome to the Streets of Rage."
                "You will have to fight your way through this level to win!")

def choose_character():
    print_pause("Please choose your character:")
    character = input("1. Axel\n"
                        "2. Blaze\n"
                        "3. Adam\n")

    print_pause(f"You have chosen {character}\n"
                "a great warrior indeed")

    print_pause(f"{character}, you have landed on the Streets of Rage.\n ")

def street_choice():
    print_pause("Please choose the name of the street you would like travel to.")
    street = input("East street, West street, South street\n").lower()

    if "east" in street:
        east_street()
    elif 'west' in street:
        west_street()
    elif 'south' in street:
        south_street()


def east_street():
        print_pause("You take the train to East street, which "
                    "contains a small shopping precint.")
        if "Broadsword" in items:
            print_pause("The weapon store owner gives you \n"
                        "a thumbs up, you are well equiped \n"
                        "for what may lie ahead. \n")
            street_choice()

        else:
            print_pause("You see a weapons store, and enter right away "
                        "The store owner asks what you need\n")
            print_pause("You ask, 'What weapon will serve me well? "
                        "on these mean streets'\n")
            print_pause("The store owner hands you a Broadsword."
                        "'This should serve you well, but to prove effective,"
                        "it requires a power cell found in another street'\n")
            items.append("Broadsword")
        print_pause("You now decide to travel to another part of town.")
        street_choice()


def west_street():
        print_pause("You take the tram to West street, where "
                    "you are drawn to a glowing haze of light .")
        if "Power cell" in items:
            print_pause("The necromancer suggests you head to the South, "
                        "where some dangerous creatured have been "
                        "terrorising the locals.")
            street_choice()

        elif "Broadsword" in items:
                print_pause("You meet a necromancer, who gifts you with a "
                            "Power cell.  This enhances your swords power ."
                            "This also gives you great visibility at night.")
                items.append("Power cell")
                street_choice()

        else:
            print_pause("The necromancer greets you sternly "
                        "'I am the necromancer, the enhancer of"
                        "weapons.  Only come back to me once your"
                        "have your weapon.  Stop wasting my time!'")
        print_pause("You now decide to travel to another part of town.")
        street_choice()


def south_street():
        print_pause("You take the train to South street, which "
                    "is shrouded in an eerie darkness.")
        print_pause("After a few moments, you here a frigtening roar.")
        print_pause("Here the dangerous creatures lurk")
        if "Power cell" in items:
            print_pause("Your power cell provides some much needed light ")
            if "Broadsword" in items:
                some_function()
                print_pause("You win!")
                play_again()
            else:
                print_pause("You are attacked without warning and have no "
                            "weapon to defend yourself from the monster attack. ")
                print_pause("You flee from the scene, and just manage to escape")
            street_choice()

        else:
            print_pause("With no power cell to help to see, or weapon to defend yourself"
                        ", you are easily defeated.")
            print_pause("Game Over!")
            play_again()

def play_again():
    print_pause("would you like to play again?:")
    play = input("y/n?")
    if play == "y":
        start()

    elif play == "n":
        print("Goodbye ")
        sys.exit(0)


def play_game():
    items = []
    start()
    choose_character()
    street_choice()


play_game()
