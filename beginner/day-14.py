from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Format the account data into printable format."""
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
    return f"{account_name}, a {account_descr}, and {account_country}"

def check_answer(guess,a_followers,b_followers):
    """Take the user guess and followers counts and returns if the guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0


# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Compare B: {format_data(account_b)}")

# Ask user for a guess.
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct.
## Get follower count of each account
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

is_correct = check_answer(guess,a_follower_count,b_follower_count)

# Give user feedback on their guess.
if is_correct:
    score += 1
    print(f"You've got it! You are correct! {score}")
else:
    print(f"You've got it! You are wrong! final score {score}")

# Score Keeping.

# Make the game repeatable.

# Making account at position B become the next account a position A.

# Clear the screen between rounds.
