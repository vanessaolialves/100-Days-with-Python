# Print the logo
# Choice one of the item in the list that will be the A
# Print other art
# Choice other item in the list to be the B
# Always the new A will be B older, and the B will be a new choice
# Always verify which item is higher


from art import logo, vs
from game_data import data
import random

def game_winner_def(follower_A, follower_B):

    choice = input("Who has more followers? Type 'A' or 'B': ")

    # while choice != 'A' or choice != 'B':
    #     choice = input("Who has more followers? Type 'A' or 'B': ")

    if follower_A > follower_B:
        return choice == 'A'
    return choice == 'B'




def options(length_data, index_A):


    COLUMN_NAME = 'name'
    COLUMN_FOLLOWER = 'follower_count'
    COLUMN_DESCRIPTION = 'description'
    COLUMN_COUNTRY = 'country'

    name_A = data[index_A][COLUMN_NAME]
    follower_A = data[index_A][COLUMN_FOLLOWER]
    description_A = data[index_A][COLUMN_DESCRIPTION]
    country_A = data[index_A][COLUMN_COUNTRY]

    print(f"Compare A: {name_A}, a {description_A}, from {country_A}.")

    print(vs)

    index_B = index_A

    while(index_B == index_A):
        index_B = random.randint(0, length_data-1)

    name_B = data[index_B][COLUMN_NAME]
    follower_B = data[index_B][COLUMN_FOLLOWER]
    description_B = data[index_B][COLUMN_DESCRIPTION]
    country_B = data[index_B][COLUMN_COUNTRY]

    print(f"Against B: {name_B}, a {description_B}, from {country_B}.")

    answer = game_winner_def(follower_A, follower_B)

    return index_B, answer


def higher_lower_game():

    print(logo)

    length_data = len(data)
    score = 0

    index_A = random.randint(0, length_data-1)
    is_winner = True

    while is_winner:
        index_A, is_winner = options(length_data, index_A)
        if is_winner:
            score += 1
            print(f"You're right! Current score: {score}.")

    print(f"Sorry, that's wrong. Final score: {score}.")


higher_lower_game()
