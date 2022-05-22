"""Program: Print number of trees planted for each kid
@Author: Sefa BILSEL"""

personnel_number = int(input("Please enter the personnel number: "))
total = 0
for i in range(personnel_number):
    kids = int(input("Enter number of kids you have: "))
    total += kids
    print(f"We have planted {kids} trees")
print(f"{total} are planted in total")
