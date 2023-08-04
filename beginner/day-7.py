
# Random choose word
import random

word_list = ["baboon","udit","gurani"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display += "_"

end_of_game = False
life = 3

while not end_of_game:
 guess = input("Guess a letter:").lower()
 for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
       display[position] = letter

 print(display)

 if "_" not in display:
    end_of_game = True
    print("You win")