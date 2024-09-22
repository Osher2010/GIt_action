import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number!")

guessing_game()
git 
