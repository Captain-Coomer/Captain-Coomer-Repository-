"""
Program: Find Salary Based on Number of Kids and Age
@Author: Sefa S. BILSEL
"""

# Entering the values

name_surname = (input("Please Enter Your Name and Surname: "))
age = int(input("Please Enter Your Age: "))
salary = float(input("Please Enter Your Salary: "))
number_of_kids = int(input("Please Enter How Many Children You Have: "))

# Checking the conditions for the extra money

if age < 45 and number_of_kids < 3:
    print(salary + (250 * number_of_kids))
elif age < 45 and number_of_kids >= 3:
    print(salary + (200 * number_of_kids))
else:
    print(salary + 500)
