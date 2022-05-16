"""
Program: Find if the students passed the exam
@Author : Sefa S. BILSEL
"""

# Entering the scores

Visa1 = int(input("Please enter 1st Visa Score: "))
Visa2 = int(input("Please enter 2nd Visa Score: "))
Final = int(input("Please enter the final Score: "))

Average_Score = ((Visa1 + Visa2)/2)*0.4 + Final*0.6

# Making sure that Scores are between 0 and 100 and Calculating the final result

if (Visa1 > 100) or (Visa1 < 0):
    print("Please enter a value between 0 and 100 for Visa 1")
    if (Visa2 > 100) or (Visa2 < 0):
        print("Please enter a value between 0 and 100 for Visa 2")
        if (Final > 100) or (Final < 0):
            print("Please enter a value between 0 and 100 for Final")
else:
    print(Average_Score, "is the total average.")
    if Average_Score >= 85:
        print("Excellent")
    elif Average_Score >= 70:
        print("Good")
    elif Average_Score >= 45:
        print("Passed")
    elif Average_Score >= 0:
        print("Failed")
