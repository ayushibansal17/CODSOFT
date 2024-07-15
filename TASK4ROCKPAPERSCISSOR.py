import random

# Function to determine the winner of Rock, Paper, Scissors
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to display choices and result
def display_choices_and_result(user_choice, computer_choice, result):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

# Function to update scores
def update_scores(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

# Function to ask user if they want to play again
def play_again():
    play = input("Do you want to play again? (yes/no): ").lower()
    return play == 'yes'

# Initialize scores
user_score = 0
computer_score = 0

# Welcome message and game loop
print("Welcome to Rock, Paper, Scissors Game!")
while True:
    # Prompt user for choice
    user_choice = input("\nChoose one: rock, paper, or scissors: ").lower()
    
    # Validate user input
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    
    # Generate computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display choices and result
    display_choices_and_result(user_choice, computer_choice, result)
    
    # Update scores
    update_scores(result)
    
    # Display current scores
    print(f"\nScores - You: {user_score}, Computer: {computer_score}")
    
    # Ask if the user wants to play again
    if not play_again():
        print("\nThank you for playing!")
        break
