"""
Program: Generate 20 random numbers between 1-200 and assign them to a list called numbers and
Prevent the number from being added to the list again.
@Author: Sefa BILSEL
"""

import random
numbers = list()
while len(numbers) < 20:
    ab = random.randint(1, 201)
    if ab not in numbers:
        numbers.append(ab)
print(numbers)