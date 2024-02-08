"""Revision Task - Sandwich Maker
by Ethan Wong

No error checking"""


def print_options(menu):
    for option in menu:
        print(f"{option} {'':.<5} ${menu[option]:.2f}")
    print(f"None {'':.<5} $0.00")


def print_selection(menu, bread, meats, garnishes):
    print("Bread")
    print(f" {bread} {'':.<5} ${menu["bread"][bread]:.2f}")

    print("Meats")
    for meat in meats:
        print(f" {meat} {'':.<5} ${menu["meat"][meat]:.2f}")

    print("Garnishes")
    for garnish in garnishes:
        print(f" {garnish} {'':.<5} ${menu["garnish"][garnish]:.2f}")


def select_bread(bread_menu):
    print_options(bread_menu)
    while True:
        user = input("Select a bread option: ").strip().title()
        if user in bread_menu.keys():
            print(f"You have selected {user} bread")
            return bread_menu[user]
        else:
            print("Please enter a valid option")


def select_ingredients(ingredient_menu, ingredient):
    menu = ingredient_menu
    print_options(menu)
    print(f"Skip ..... (no {ingredient})")
    print(f"Done")

    selection = []

    while True:
        user = input(f"Select a(nother) {ingredient} option: ").strip().title()
        if user in menu.keys():
            print(f"You have selected {user} {ingredient}")
            selection.append(ingredient_menu[user])
            return selection
        elif user == "Done":
            print(f"")
        elif user in ("Skip", "X", "Cancel", "N", "No"):
            return []
        else:
            print("Please enter a valid option")


MY_MENU = {
    "bread": {
        "Wholemeal": 1.00,
        "White": 0.80,
        "Cheesy White": 1.20,
        "Gluten Free": 1.40
    },
    "meat": {
        "Chicken": 2.69,
        "Beef": 3.0,
        "Salami": 4.0,
        "Vegan Slice": 3.3
    },
    "garnish": {
        "Onion": 1.69,
        "Tomato": 1.0,
        "Lettuce": 2.0,
        "Cheese": 2.5
    }
}

bread = select_bread(MY_MENU["bread"])
print()
ingredients = select_ingredients(MY_MENU["meat"], "meat")
print()
garnishes = select_ingredients(MY_MENU["garnish"], "garnish")
print()
print_selection(MY_MENU, bread, ingredients, garnishes)



