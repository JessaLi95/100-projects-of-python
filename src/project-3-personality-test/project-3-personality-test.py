print('''
                        \   |    /
                    `.   \  '   /   .'
                      `. .-*""*-. .'
                  "*-._ /.*"  "*.\ _.-*"
                       :    ;      ____
                  """"':    ..    ;
                  _.-*" \ `.__.' / "*-._
                      .' `-.__.-' `.
                    .'   /   .  \   `.
                        /    |   \\
                       '     |    `
        .-.
        |.|
      /)|`|(\\
     (.(|'|)`)
  ~~~~`\`'./'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        |.|           ~~
        |`|                            ~~
       ,|'|.                   ~~
        "'"
             ~~
''')
print("This project works specifically for Python 3.10.\n"
      "------------------------------------------------")

print(
    "This is a simple personality test created by Jiaze Li, please answer the following questions to reveal your order\nto specific life aspects.")
print("...")

name = input("Welcome, please type in your name: \n")
print(f"Hi, {name}, imagine you are waking in a desert with 5 animals:【Horse】,【Sheep】,【Cow】,【Lion】,【Monkey】")
print("...")

print("Because of limited water and foods, you are going to have to leave one of the animals behind.")
print("...")

menu_options = {
    1: 'Horse',
    2: 'Sheep',
    3: 'Cow',
    4: 'Monkey',
    5: 'Lion',
    6: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def horse():
    print('''
                >>\.
               /_  )`.
              /  _)`^)`.   _.---. _
             (_,' \  `^-)""      `.\\
                   |              | \\
                   \              / |
                  / \  /.___.'\  (\ (_
                 < ,"||     \ |`. \`-'
                  \\ ()      )|  )/
                  |_>|>     /_] //
                    /_]        /_]
    ''')
    print('"If you abandon your horse first, it means that during your life journey, work is nothing more than the basic\n'
          'expenses needed to maintain your life, and you are not operating your job as a dream or a passion."\n')


def sheep():
    print('''
               __  _
           .-.'  `; `-._  __  _
          (_,         .-:'  `; `-._
        ,'o"(        (_,           )
       (__,-'      ,'o"(            )>
          (       (__,-'            )
           `-'._.--._(             )
              |||  |||`-'._.--._.-'
                         |||  |||
    ''')
    print('"Sheep represents lovers or marriage. The person who discards the sheep first means that you will sacrifice\n'
          'love first when it comes to a difficult choice."\n')


def cow():
    print('''
         _ (.".) _
        '-'/. .\\'-'
          /_   _\     _...._
         (` o o `)---`      '.
          /"---"`             \\
          |            /     ;|
          |           |      ||
           \\\\   \  \  \     /\\\\
            \`;-'| |-.-'-,  \ |)
             ( | ( | `-uu ( |
              ||  ||    || ||
             /_( /_(   /_(/_(
        ''')
    print('"Cow represents parents and relatives. Do not blame yourself if you abandon cow first, it may means that you\n'
          'are an independent person."\n')


def monkey():
    print('''
                        .-"""-.
                       _/-=-.   \\
                      (_|a a/   |_
                       / "  \   ,_)
                  _    \`=' /__/
                 / \_  .;--'  `-.
                 \___)//      ,  \\
                  \ \/;        \  \\
                   \_.|         | |
                    .-\ '     _/_/
                  .'  _;.    (_  \\
                 /  .'   `\   \\\\_/
                |_ /       |  |\\\\
               /  _)       /  / ||
              /  /       _/  /  //
              \_/       ( `-/  ||
                        /  /   \\\\ .-.
                        \_/     \\'-'/
                                 `"`
        ''')
    print('"Monkey represents friendship. You may think that friends are negligible compares to family or lover."\n')


def lion():
    print('''
                               ,%%%%%%%,
                            ,%%/\%%%%/\%,
                           ,%%%\c "" J/%%,
      %.                   %%%%/ d  b \%%%
      `%%.         __      %%%%    _  |%%%
       `%%      .-'  `"~--"`%%%%(=_Y_=)%%'
        //    .'     `.     `%%%%`\\7/%%%'____
       ((    /         ;      `%%%%%%%'____)))
       `.`--'         ,'   _,`-._____`-,
         `"""`._____  `--,`          `)))
                    `~"-)))
    ''')
    print('"Lion represents rational thinking. You might be a bit sensitive when facing big decision."\n')


def end():
    print("Thanks for your time, hope you had fun in this test :)\n")


while True:
    print_menu()
    option = ""
    try:
        option = int(input("Which animal would you give up first?\n"))
    except:
        print('Wrong input. Please enter a number...')
        # Check the answer corresponding to the option
    match option:
        case 1:
            horse()
        case 2:
            sheep()
        case 3:
            cow()
        case 4:
            monkey()
        case 5:
            lion()
        case 6:
            end()
            exit()
        case _:
            print("Invalid option. Please enter a number between 1 to 6.\n")
