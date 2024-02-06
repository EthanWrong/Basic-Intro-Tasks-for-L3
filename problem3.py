"""Problem 3 - E"""

sentence = input("Enter a sentence: ")
num_e = 0
for i in sentence:
    if i.lower() == "e":
        num_e += 1
print(num_e)
