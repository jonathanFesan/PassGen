import random
import string

cont = "y"
while cont == "y":
    leng_pass = int(input("Enter the number of characters for the password: "))
    # Printing the options menu
    print("""##### OPTIONS MENU #####
    1- Numerical
    2- Alphanumeric 
    3- Special Characters
    4- Exit
    """)
    # Variable to control the loop
    sel = "run"
    char = []
    while sel == "run":
        option = int(input("Enter an option: "))
        if option == 1:
            char += string.digits  # Add numerical digits to the character list
            sel = "fns"
        elif option == 2:
            char += string.digits  # Add numerical digits to the character list
            char += string.ascii_letters  # Add ASCII letters (uppercase and lowercase) to the character list
            sel = "fns"
        elif option == 3:
            char += string.digits
            char += string.ascii_letters
            char += string.punctuation  # Add special characters to the character list
            sel = "fns"
        elif option == 4:
            print("Exiting")
            break
        else:
            print("Invalid option, please try again!")

    # Create a list for the password
    password = []
    # Fill the password character list
    for i in range(leng_pass):
        # Create a variable that contains a random value from the character list created in the if structure
        randomchar = random.choice(char)
        # For each value in the length list, add a random value to the list
        password.append(randomchar)
    print("Your strong password is:", "".join(password))  # The join() method concatenates the characters into a string.
    cont = input("Generate another password? Enter y/n: ")

print("Password generator finished")
