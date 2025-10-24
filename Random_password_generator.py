import random
import string


while True:
    try:
        length = int(input("Enter the length of the password: "))
        break

    except ValueError:
        print("The length of the password must be a number")

while True:
    letter = input("Do you want to use letters? (y/n)").lower()
    if letter == "y" or letter == "n":
        break
    else:
        print("Enter 'y' for yes and 'n' for no")

while True:
    number = input("Do you want to use numbers? (y/n)").lower()
    if number == "y" or number == "n":
        break
    else:
        print("Enter 'y' for yes and 'n' for no")

while True:
    symbol = input("Do you want to use symbols? (y/n)").lower()
    if symbol == "y" or symbol == "n":
        break
    else:
        print("Enter 'y' for yes and 'n' for no")

characters = ""
if letter == "y":
    characters += string.ascii_letters
if number == "y":
    characters += string.digits
if symbol == "y":
    characters += string.punctuation

if not characters:
    print("Error: No character type was selected")
    quit()

password = ""
for i in range(length):
    password += random.choice(characters)

print(f"Generated password: {password}")

        



    
    

    
    