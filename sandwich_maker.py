"""Revision Task - Sandwich Maker
by Ethan Wong

No error checking"""


def select_bread(bread_menu):
    for i, option in enumerate(bread_menu):
        print(f"{i+1} - {option} {'':.<5} ${bread_menu[option]}")


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

select_bread(MY_MENU["bread"])


