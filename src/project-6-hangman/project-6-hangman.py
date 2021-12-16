# Step 3
import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

# Testing code
print(hangman_art.logo)
# print(f'Pssst, the solution is {chosen_word}.')

lives = 6

# Create blank list
display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)

while lives > 0:
    player_guess = input("Guess a letter: ").lower()
    if player_guess in display:
        print(f"You've typed in {player_guess} before")
    if player_guess in chosen_word:
        for i in range(0, len(chosen_word)):
            if chosen_word[i] == player_guess:
                display[i] = player_guess
    else:
        lives -= 1
        print(f"The word {player_guess} is not in the word, you lose a life.")
        print(hangman_art.stages[lives])
    print(display)
    if display.count("_") == 0:
        print("You win!")
        break
if lives <= 0:
    print(f"You lose! The word is {chosen_word}")
