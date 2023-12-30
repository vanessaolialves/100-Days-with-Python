from game_data import data
import random
from art import logo, vs
from replit import clear

# Generate a random account from the game data.
def get_random_account():
    """Get data from random account"""
    return random.choice(data)

# Format account data into printable format.
def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"

# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    # Display art
    print(logo)

    # Score Keeping.
    score = 0
    game_should_continue = True

    # Generate a random account from the game data.
    account_b = get_random_account()

    # Make the game repeatable.
    while game_should_continue:

        # Making account at position B become the next account at position A
        ## Make B become the next A.
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        # Format account data into printable format.
        print(f"Compare A: {format_data(account_a)}.")

        # Add art.
        print(vs)

        # Format account data into printable format.
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct.
        ## Get follower count of each account.
        ## Use if statement to check if user is correct.
        is_correct = check_answer(guess, a_follower_count, b_follower_count)


        # Clear screen between rounds.
        clear()
        # Add art.
        print(logo)

        # Give user Feedback on their guess.
        if is_correct:
            # Score Keeping.
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers?

# Suppose you just started the game and you are comparing the followers of A - Instagram (364k)
# to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct.
# However, the subsequent comparison should be between Selena Gomez (the new A) and someone else.
# The reason is that everything in our list has fewer followers than Instagram.
# If we were to keep Instagram as part of the comparison (as choice A)
# then Instagram would stay there for the rest of the game.
# This would be quite boring. By swapping choice B for A each round,
# we avoid a situation where the number of followers of choice A keeps going up over the course of the game.
# Hope that makes sense :-)

'''
