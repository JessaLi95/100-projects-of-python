#1. Create a greeting for your program.
print('Welcome to the "What to eat" generator: ')
#2. Ask the user for their fav flavor.
flavor = input("Which flavors of dishes you like the most? e.g. salty/sour/sweet\n")
#3. Ask the user for their fav meat.
meat = input("What is your fav meat?\n")
#4. Ask the user for their fav cooking method.
method = input("What is your fav method of cooking? e.g. fry/roast/steam\n")
#5. Ask the user for their fav veg.
veg = input("What is your fav vegetable?\n")
#6. Combine the preference and generate the dish
print("Maybe try: " + flavor + " " + meat + " " + method + " with " + veg + " for today")