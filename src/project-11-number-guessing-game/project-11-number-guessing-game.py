import random

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")
answer = random.randint(1, 100)
# print(f"This answer is {answer}.\n")
difficulty = input('Choose a difficulty type "easy" or "hard"\n')
attempt_number = 10
if difficulty == "hard":
    attempt_number = 5


def compare():
    global attempt_number
    game_continue = True
    while game_continue:
        print(f"You have {attempt_number} attempts remaining to guess the number.\n")
        if attempt_number == 0:
            print("【Game over】")
            game_continue = False
        else:
            player_guess = int(input("Make a guess: "))
            if player_guess == answer:
                print("【You are right】")
                game_continue = False
            else:
                if player_guess > answer:
                    print("【Too high, guess again】\n")
                elif player_guess < answer:
                    print("【Too low, guess again】\n")
                attempt_number -= 1


compare()
