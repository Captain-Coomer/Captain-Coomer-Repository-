"""
Program:
@Author: Sefa BILSEL
"""

import random
numbers = list()
while len(numbers) < 20:
    ab = random.randint(1, 201)
    if ab not in numbers:
        numbers.append(ab)
print(numbers)