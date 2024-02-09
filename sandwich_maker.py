"""Revision Task - Sandwich Maker
by Ethan Wong

Known bugs:
- selecting no bread first, and then later adding a bread, will cause the program to crash"""



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


def print_options(options):
    for option in options:
        print(f" {option} {'':.<5} ${options[option]:.2f}")
    print("Enter 'X' to move on")


def select_ingredient(menu, ingredient, limit=100):
    selection = []
    print(f"{ingredient.title()} - Limit: {limit}")
    print_options(menu[ingredient])
    while True:
        user = input(f"Select a {ingredient}: ").strip().title()
        if user in menu[ingredient].keys():
            selection.append([user, menu[ingredient][user]])
        elif user == "X":
            return selection
        else:
            print("Please enter a valid option")

        if len(selection) >= limit:
            return selection


def print_order(order):
    cost = 0.0
    print(f"Your Order:")
    for item in order:
        cost += item[1]
        print(f" {item[0]} {'':.<5} ${item[1]:.2f}")
    print(f" Total Cost: ${cost:.2f}")
    print()


def prompt_edit():
    print("Edit Order:\n"
          " Enter the name of the item you would like to remove\n"
          " Enter 'bread' if you would like to change the bread type\n"
          " Enter 'meat' or 'garnish' if you would like to add more\n"
          " Enter 'Done' if you are happy with your order")


def edit_order(order, menu, prompt_needed=True):
    while True:
        if prompt_needed:
            prompt_edit()
        user = input(" > ").lower()
        print()

        prompt_needed = False

        item_names = []
        for item in order:
            item_names.append(item[0].lower())

        if user in item_names:
            order.pop(item_names.index(user))
            print(f"You have removed {user.title()} from your order.")
        elif user == "bread":
            del order[0]
            order = select_ingredient(menu, "bread", 1) + order
            print(f"You have selected {order[0][0]} bread.")
            prompt_needed = True
        elif user in ("meat", "garnish"):
            order += (select_ingredient(menu, user))
            print(f"You have added {user.title()} to your order")
            prompt_needed = True
        elif user in ("done", "complete", "finish", "end"):
            print_order(order)
            return order
        elif user == "?":
            prompt_needed = True
        else:
            print("Please enter a valid option (?)")
            prompt_needed = True

        print()
        print_order(order)

# main routine


print("Welcome to Sandwhich Maker, where all your sandwich dreams come true.")
print()
my_bread = select_ingredient(MY_MENU, "bread", 1)
print()
my_meat = select_ingredient(MY_MENU, "meat")
print()
my_garnish = select_ingredient(MY_MENU, "garnish")
print()

my_order = my_bread + my_meat + my_garnish
print_order(my_order)

my_order = edit_order(my_order, MY_MENU)

print("Thank you for using Sandwich Maker")
