"""Problem 5 - Error 53"""

numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]

numbers = [53 if num == 353 else num for num in numbers]

# for i, num in enumerate(numbers):
#     if num == 353:
#         numbers[i] = 53

print(numbers)
