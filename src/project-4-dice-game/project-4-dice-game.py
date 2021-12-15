print('''
 ____________________________________________________
|: : : : : : : : : : : : : : : : : : : : : : : : : ::|
| : : : : : : : : :_________________________: : : : :|
|: : : : : : : : :)                         (: : :: :|
| : : : : : : : : )     $Jiaze's Casino$    ( :::  ::|
| : : ::__________)_________________________(________|
| _____ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
| /_\ '.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.
|:=|=: |                  _________                  |
|: : : |   ______    _  .'         '.  _    ______   |
|======| .' ,|,  '. /_\ |           | /_\ .'  ,|, '. |
|Lounge| | ;;;;;  | =|= |           | =|= |  ;;;;; | |
|<---  | |_';;;'_$|     |  n______  |     |$_';;;'_| |
|      | |_|-;-|__|     |-|_______|-|     |__|-;-|_| |
|      | |________|     |           |     |________| |
|      |                |           |                |
|______|________________|           |________________|
''')

print("Welcome to Jiaze's casino, if your dice has a smaller number than the computer ☞【buy Jiaze a drink】")

dice1 = '''
          _____
         / .  /\\
        /____/..\\
        \\'  '\  /
         \\'__'\/
'''
dice2 = '''
          _____
         / .. /\\
        /____/..\\
        \\'  '\  /
         \\'__'\/
'''
dice3 = '''
          _____
         / .. /\\
        /__'_/..\\
        \\'  '\  /
         \\'__'\/
'''
dice4 = '''
          _____
         / .. /\\
        /_''_/..\\
        \\'  '\  /
         \\'__'\/
'''
dice5 = '''
          _____
         / .../\\
        /_''_/..\\
        \\'  '\  /
         \\'__'\/
'''
dice6 = '''
          _____
         /... /\\
        /_```/..\\
        \\'  '\  /
         \\'__'\/
'''
dicePattern = [dice1, dice2, dice3, dice4, dice5, dice6]

import random

menu_options = {
    1: "Play",
    2: "Help",
    3: "Exit",
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


# A random seed is a starting point in generating random numbers. A random seed specifies the start point when a
# computer generates a random number sequence. This can be any number, but it usually comes from seconds on a
# computer system's clock


def play():
    test_seed = int(input("Create a seed number: \n"))
    random.seed(test_seed)

    playerDice = random.randint(1, 6)
    print(dicePattern[playerDice - 1])
    print(f"You diced【{playerDice}】\n")

    computerDice = random.randint(1, 6)
    print(dicePattern[computerDice - 1])
    print(f"The computer diced【{computerDice}】\n")

    if playerDice > computerDice:
        print('"You win!"\n')
    elif playerDice < computerDice:
        print('"You lose!"\n')
    else:
        print('"It is a draw, play again."\n')


def howtoplay():
    print('"Do you mean you do not know how to play【Rock Paper Scissors】???"\n')


def leave():
    print("Thanks for your time, hope you had fun.\n")


while True:
    print_menu()
    option = input("Ready to start your game?\n")

    if option == "1":
        play()
    elif option == "2":
        howtoplay()
    elif option == "3":
        leave()
        exit()
    else:
        print("Invalid option, type in 1, 2, or 3.\n")
