"""
Program: Find the odd numbers between 10 and 100
@Author: Sefa BILSEL
"""

numbers = list(range(10, 101))
for x in numbers:
    if x % 2 != 0:
        print(x, end=", ")

# 2nd method

odd_numbers = list()
for i in range(11, 101, 2):
    odd_numbers.append(i)
print(odd_numbers)