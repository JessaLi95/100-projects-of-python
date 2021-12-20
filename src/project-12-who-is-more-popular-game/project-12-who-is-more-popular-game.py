from art import logo, vs
from game_data import data
import random

player_score = 0
player_a = None
player_b = None


def choose_from_data():
    """choose random celebrity from database, and return in dictionary format."""
    chosen_info = random.choice(data)
    return chosen_info


def compare_choice(player_choice):
    """Check if the user's answer matches the data."""
    a_bigger = player_a['follower_count'] > player_b['follower_count']
    if player_choice == 'a':
        return a_bigger
    elif player_choice == 'b':
        return not a_bigger


def print_player(player, declaration):
    """Print our the information in a printable format."""
    print(f"{declaration}: {player['name']}, a {player['description']}, from {player['country']}.")
    # print(player['follower_count'])


def game_loop():
    """Ask if users want to loop the game if they got wrong answer."""
    global player_score
    global player_a
    global player_b
    player_a = choose_from_data()
    game_continue = True
    while game_continue:
        print(logo)

        player_b = choose_from_data()
        while player_a == player_b:
            player_b = choose_from_data()
        # We now have two different players

        print_player(player_a, "Compare A: ")

        print(vs)

        print_player(player_b, "Against B: ")

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = compare_choice(choice)

        if result == 0:
            print(f"You're wrong! Your final score is: 【{player_score}】")
            game_continue = False
        else:
            player_score += 1
            print(f"You're right! Current score is: 【{player_score}】")
            if choice == 'b':
                player_a = player_b
    loop_the_game = input("Do you want to play again? 'y' for yes, 'n' for no.").lower()
    if loop_the_game == 'y':
        game_loop()


game_loop()
