import time
import random
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)

enemies = ["Zamza", "Vehelits"]

def start():
    print_pause("Welcome to the Streets of Rage."
            "You will have to fight your way through this level to win!")

print_pause("Please choose your character:")
character = input("1. Axel\n"
                    "2. Blaze\n"
                    "3. Adam\n")

print_pause(f"You have chosen {character}\n"
                "a great warrior indeed")

while True:
    while True:

        print_pause(f"{character} You have landed on the Streets of Rage\n"
                "you must choose which area to travel to")
        response = input("East street, West street, South street\n").lower()

        if "east" in response:
            print_pause("You take the train to East street, which "
                        "contains a small shopping precint.")
            if "Broadsword" in items:
                print_pause("The weapon store owner gives you \n"
                            "a thumbs up, you are well equiped \n"
                            "for what may lie ahead. \n")
            else:
                print_pause("You see a weapons store, and enter right away "
                            "The store owner asks what you need\n")
                print_pause("You ask, 'What weapon will serve me well "
                            "on these mean streets'\n")
                print_pause("The store owner hands you a Broadsword."
                            "'This should serve you well, but to prove effective,"
                            "it requires a power cell found in another street'\n")
                items.append("Broadsword")
            print_pause("You now decide to travel to another part of town")

        elif "west" in response:
            print_pause("You take the tram to West street, where "
                        "you are drawn to a glowing haze of light .")
            if "Power cell" in items:
                print_pause("The necromancer suggests you head to the South, "
                            "where some dangerous creatured have been "
                            "terrorising the locals.")
            else:
                if "Broadsword" in items:
                    print_pause("You meet a necromancer, who gifts you with a "
                                "Power cell.  This enhances your swords power ."
                                "This also gives you great visibility at night.")
                    items.append("Power cell")
                else:
                    print_pause("The necromancer greets you sternly "
                                "'I am the necromancer, the enhancer of"
                                "weapons.  Only come back to me once your"
                                "have your weapon.  Stop wasting my time'")
            print_pause("You now decide to travel to another part of town")

        elif "south" in response:
            print_pause("You take the train to South street, which "
                        "is shrouded in an eerie darkness.")
            print_pause("After a few moments, you here a frigtening roar.")
            print_pause("Here the dangerous creatures lurk")
            if "Power cell" in items:
                print_pause("Your power cell provides some much needed light ")
                print_pause(enemy = random.choice(enemies))
                print_pause("Zamza, a powerful mutant suddenly appears, but luckily "
                            "you see him in good time, ready to anticipate his attack.")

        print_pause("Where would you like to go next?")

    start()
