## Scope ##
from random import randint

# global scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"{enemies}")


increase_enemies()
print(f"{enemies}")


# local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# check number
def check_answer(guess, answer,turn):
    if guess > answer:
        print("Too High")
        return turn - 1
    elif guess < answer:
        print("Too low.")
        return turn - 1
    else:
        print(f"you got it! the answer was {answer}")

def set_difficulty():
    level = input("Choose diffculty")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

turns = 0
# choosing the random number 1 to 100
def game():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 to 100")
    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attemps remaining to guess the number.")
    guess = 0
    while guess != answer:
        check_answer(guess,answer,turns)
        guess = int(input("Guess the number"))


game()