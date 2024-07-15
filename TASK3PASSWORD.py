import random
import string

def generate_password(length):
    # Define the character set for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Welcome message
print("Welcome to Password Generator!")

# Prompt user for password length
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate and display the password
password = generate_password(length)
print(f"Generated Password: {password}")
