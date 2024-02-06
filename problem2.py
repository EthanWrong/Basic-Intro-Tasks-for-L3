"""Problem 2 - Fishes"""

FISH = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]

print("a)")
for i in FISH:
    print(i[0])

print("\nb)")
for i in FISH:
    print(i[0:3])

print("\nc)")
max = ""
for i in FISH:
    # .replace() to ignore spaces; i.e "john dory" counts as len=8, not len=9
    if len(i.replace(" ","")) > len(max.replace(" ","")):
        max = i
print(f"The first longest word is {max}")

print("\nd)")
for i in FISH:
    if len(i.split()) > 1:
        print(i)

print("\ne)")
for i in FISH:
    if "cod" in i:
        print(i)

