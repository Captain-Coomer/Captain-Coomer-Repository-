"""
Program: User input validation using while loops
@Author: Sefa BILSEL
"""

# Registered user values

registered_username = "Sefa"
registered_password = "123"
registered_email = "sefabilsel@outlook.com"
count = 0
count_2 = 0

# Checking if username/email and password matches the registered user's info
# If the info isn't matching, asking to sign up

question1 = input("Are you already an Existing user? Please Enter Yes or No: ")
if question1.lower() == "yes":
    while count < 3:
        username = input("Please Enter your Username: ")
        password = input("Please Enter your Password: ")
        if (username == registered_username or username == registered_email) and password == registered_password:
            print("Login Successful!")
            break
        elif count == 2:
            print("Login failed 3 times in a row!")
        else:
            print("Login failed, Try again!")
        count += 1

elif question1.lower() == "no":
    while count_2 < 3:
        question2 = input("Would you like to Register, Type Yes or No: ")
        if question2.lower() == "no":
            print("Ok, have a nice day!")
            break
        elif question2.lower() == "yes":
            name = input("Enter your Real Name: ")
            surname = input("Enter your surname: ")
            email = input("Enter your email: ")
            new_username = input("Enter your Username: ")
            new_password = input("Enter your password: ")
            password_confirmation = input("Enter your password again: ")
            if password_confirmation == new_password:
                print("Good job, account creation completed!")
                break
            else:
                print("Passwords are not matching! please try again!")
        count_2 += 1
