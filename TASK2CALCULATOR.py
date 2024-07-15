# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Display welcome message
print("Welcome to Simple Calculator!")

# Prompt user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Input choice of operation
choice = input("\nEnter operation choice (1/2/3/4): ")

# Perform calculation based on user's choice
if choice == '1':
    print("\nResult:", add(num1, num2))
elif choice == '2':
    print("\nResult:", subtract(num1, num2))
elif choice == '3':
    print("\nResult:", multiply(num1, num2))
elif choice == '4':
    print("\nResult:", divide(num1, num2))
else:
    print("\nInvalid input! Please choose a valid operation (1/2/3/4).")

