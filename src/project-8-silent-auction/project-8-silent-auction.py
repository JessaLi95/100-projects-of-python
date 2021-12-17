import art
from replit import clear

# HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")

total_dic = {}

continue_count = True
while continue_count:
    name = input("What is your name?\n")
    bid = int(input("What is your bid? \n£: "))
    total_dic[name] = bid
    other_bidder = input("Are there any other bidders? Type in yes or no: \n").lower()
    if other_bidder == "yes":
        clear()
    else:
        continue_count = False

# print(total_dic)
find_max = max(total_dic, key=total_dic.get)
print(f"The winner is {find_max} with a bid of £{total_dic[find_max]}")
