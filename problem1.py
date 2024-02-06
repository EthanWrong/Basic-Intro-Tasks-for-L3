""""Problem 1 - Secret PIN"""


def check_pin(pin):
    if len(pin) != 4:
        return False
    for i in pin:
        try:
            int(i)
        except ValueError:
            return False
    return True


my_pin = input("Enter your secret 4-digit PIN: ")  # will return a string

if check_pin(my_pin):
    print(f"Your secret PIN is {my_pin}")
else:
    print("Invalid PIN")
