import art
import random

# Initial setting
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_2_cards():
    card_1 = random.choice(cards)
    card_2 = random.choice(cards)
    total_score = card_1 + card_2
    if (card_1 == 11 or card_2 == 11) and total_score > 21:
        total_score -= 10
    return [card_1, card_2, total_score]


def game_loop():
    print(art.logo)
    print("Welcome to Blackjack!")
    # Round 1, call the function and draw 2 cards, and detect the blackjack
    computer_score = draw_2_cards()
    computer_total = computer_score[2]
    computer_score_history = computer_score[0:2]
    if computer_total == 21:
        print(f"Computer's cards are {computer_score_history}, it got blackjack, you lose.\n")
    else:
        print(f"Computer's first card is 【{computer_score[0]}】.")

    player_score = draw_2_cards()
    player_total = player_score[2]
    player_score_history = player_score[0:2]
    if player_total == 21 and computer_total != 21:
        print(f"Your cards are {player_score_history}, you got blackjack, you win!\n")
    else:
        print(
            f"Your cards are {player_score_history}, your score is 【{player_total}】.\n")

    # Round 2: Computer's score, but hide the score until user finished.
    while computer_total <= 16:
        computer_card_3 = random.choice(cards)
        computer_score_history.append(computer_card_3)
        computer_total += computer_card_3

    # Round 3: Player's choice, reveal the result.
    continue_draw = True
    while continue_draw:
        another_card = input("Do you want to draw another card? 'y' for yes, 'n' for no.\n")
        if another_card == 'y':
            player_card_3 = random.choice(cards)
            player_total += player_card_3
            player_score_history.append(player_card_3)
            if player_total > 21:
                print(f"Your cards are {player_score_history}, you got 【{player_total}】, over 21, you lose.")
                continue_draw = False
            else:
                print(f"Your cards are {player_score_history}, you got 【{player_total}】.")
        if another_card == 'n':
            continue_draw = False
            print(f"Your round is finished, your cards are {player_score_history}, your total score is 【{player_total}】.")
            print(f"Computer's cards are {computer_score_history}")
            if computer_total == 21:
                print("Computer got blackjack, you lose.")
            elif 0 < (21 - computer_total) < (21 - player_total):
                print(f"Computer got 【{computer_total}】, you got 【{player_total}】, you lose.")
            elif (21 - computer_total) == (21 - player_total):
                print("It's a draw")
            elif (21 - computer_total) > (21 - player_total):
                print(f"Computer got 【{computer_total}】, you got 【{player_total}】, you win.")
            elif computer_total > 21 and player_total < 21:
                print(f"Computer got 【{computer_total}】, you got 【{player_total}】, computer overflow, you win.")

    # Want to restart?
    restart = input("Do you want to play again? 'y' for yes, 'n' for no.\n")
    if restart == 'y':
        game_loop()


game_loop()
