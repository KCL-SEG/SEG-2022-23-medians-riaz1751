"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

length = len(numbers)
numbers.sort()

if (length % 2) == 1:
    median = numbers[length // 2]
else:
    median = (numbers[(length // 2) - 1] + numbers[length // 2]) / 2

print(median)
