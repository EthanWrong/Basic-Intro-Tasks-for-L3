"""Problem 4 - Character searc"""

char = input("Enter a character (1 letter) to be found: ")
char = char[0]
sentence = input("Enter a sentence: ")
num_char = 0
for i in sentence:
    if i == char:
        num_char += 1
print(num_char)
