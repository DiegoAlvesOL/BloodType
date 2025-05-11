# Name: Diego Alves de Oliveira
# Student ID: 78952
# Email: 78952@student.dorset-college.ie
import time

# List of valid blood types used for input validation.
valid_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# The following lists represent, for each blood type, the compatible donor types.
receiver_Aplus = ["A+", "A-", "O+", "O-"]
receiver_Aminus = ["A-", "O-"]
receiver_Bplus = ["B+", "B-", "O+", "O-"]
receiver_Bminus = ["B-", "O-"]
receiver_ABplus = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
receiver_ABminus = ["A-", "B-", "AB-", "O-"]
receiver_Oplus = ["O+", "O-"]
receiver_Ominus = ["O-"]

# The following lists represent, for each blood type, which types can receive donations from it.
donors_Aplus = ["A+", "AB+"]
donors_Aminus = ["A+", "A-", "AB+", "AB-"]
donors_Bplus = ["B+", "AB+"]
donors_Bminus = ["B+", "B-", "AB+", ]
donors_ABplus = ["AB+"]
donors_ABminus = ["AB+", "AB-"]
donors_Oplus = ["O+", "A+", "B+", "AB+"]
donors_Ominus = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# This function checks whether the blood type provided by the user is valid
# by verifying its presence in the list of allowed types.
def valid_blood_type(blood_user):
    if blood_user in valid_types:
        return True
    else:
        return False

# This function receives the blood type entered by the user and returns
# the list of compatible donor types according to compatibility rules.
def get_donation (blood_user):
    if blood_user == "A+":
        return receiver_Aplus
    elif blood_user == "A-":
        return receiver_Aminus
    elif blood_user == "B+":
        return receiver_Bplus
    elif blood_user == "B-":
        return receiver_Bminus
    elif blood_user == "AB+":
        return receiver_ABplus
    elif blood_user == "AB-":
        return receiver_ABminus
    elif blood_user == "O+":
        return receiver_Oplus
    elif blood_user == "O-":
        return receiver_Ominus

# This function receives the blood type entered by the user and returns
# a list of blood types that can receive donations from it.
def receives_donation (blood_user):
    if blood_user == "A+":
        return donors_Aplus
    elif blood_user == "A-":
        return donors_Aminus
    elif blood_user == "B+":
        return donors_Bplus
    elif blood_user == "B-":
        return donors_Bminus
    elif blood_user == "AB+":
        return donors_ABplus
    elif blood_user == "AB-":
        return donors_ABminus
    elif blood_user == "O+":
        return donors_Oplus
    elif blood_user == "O-":
        return donors_Ominus

# Welcome message.
# print("+","-"*50 ,"+")
# print("|  Welcome to the Blood Type Compatibility Checker!  |")
# print("+","-"*50,"+\n")
#
# # Main program loop that displays the menu and runs until the user chooses to exit.
# while True:
#     print("+","-"*50,"+")
#     print("| Choose an option: "," "*31, "|")
#     print("| 1. Check what type of blood you can recive."," "*6, "|")
#     print("| 2. Check which blood type you can donate to."," "*5, "|")
#     print("| 3. Exit the program."," "*29, "|")
#     print("+","-"*50,"+\n")
#
#     # Captures the user's choice and applies .strip() to remove extra spaces at the beginning or end of the entry.
#     choice = input("Enter your choice 1,2 or 3: ").strip()
#     if choice == "3":
#         print("+","-"*43,"+")
#         print("| Thank you for using the BloodType. Goodbye! |")
#         print("+","-"*43,"+")
#         break
#
#     # If the user types 1 they will fall into this structure which will ask them to type their blood type.
#     # The input is treated with .upper(), .strip() and .replace() to ensure that:
#     # - all letters are capitalised
#     # - spaces at the beginning, middle and end are removed
#     elif choice == "1":
#         blood_user = input("Please, enter with your blood type: ").upper().strip().replace(" ", "")
#         if not valid_blood_type(blood_user):
#             print("+","-"*38,"+")
#             print("| The blood type you entered is invalid. |")
#             print("+","-"*38,"+\n")
#         else:
#             donors = get_donation(blood_user)
#             print("Please wait a moment while we process your information...")
#             for i in range(5,-1,-1):
#                 print(i)
#                 time.sleep(0.5)
#             print("-"*103)
#             print(" Your blood type is {}, you can receive blood from: {}".format(blood_user, donors))
#             print("-"*102,"\n")
#
#     # If the user chooses option 2, the same entry and validation process is carried out.
#     elif choice == "2":
#         blood_user = input("Please, enter with your blood type: ").upper().strip().replace(" ", "")
#         if not valid_blood_type(blood_user):
#             print("+","-"*38,"+")
#             print("| The blood type you entered is invalid. |")
#             print("+","-"*38,"+\n")
#         else:
#             receiver = receives_donation(blood_user)
#             for j in range(5,-1,-1):
#                 print(j)
#                 time.sleep(0.5)
#             print("-"*102)
#             print("Your blood type is {}, and you can donate blood to: {}".format(blood_user,receiver))
#             print("-"*102,"\n")
#
#     # If the user enters an invalid option (other than 1, 2 or 3), an error message will be displayed.
#     else:
#         print("+","-"*68,"+")
#         print("| Invalid option! Please choose one of the options listed in the menu. |")
#         print("+","-"*68,"+\n")