# Final Project: The number guessing game
import random

print("Welcome to the Number Guessing Game!!!")
print("I'm thinking of a number between 1 and 100.")
level_game = input("Choose a difficulty. Type 'easy' or 'hard': ")

chances = 5
if level_game == 'easy':
    chances += 5

guess_number = random.randint(1, 100)
is_win_gain = False

while chances > 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    my_tried = int(input("Make a guess: "))
    if guess_number == my_tried:
        is_win_gain = True
        chances = 0
    elif guess_number > my_tried:
        print("Too low.")
        print("Guess again.")
    else:
        print("Too high.")
        print("Guess again.")
    chances -= 1

if is_win_gain:
    print(f"You got it! The answer was {guess_number}.")
else:
    print("You've run out of guesses, you lose.")
