from data import MENU, resources

machine_is_on = True
money_in_machine = 0
resources_update = resources
resources_update["money"] = 0


# TODO 4: After customer placed orders, check resources.
def is_enough_resource():
    enough_resources = True
    for resources_name in "water", "milk", "coffee":
        if MENU[user_input]["ingredients"][resources_name] > resources_update[resources_name]:
            print(f"Not enough {resources_name}")
            enough_resources = False
    return enough_resources


def make_coffee(coffee_name):
    resources_update["water"] -= MENU[coffee_name]["ingredients"]["water"]
    resources_update["milk"] -= MENU[coffee_name]["ingredients"]["milk"]
    resources_update["coffee"] -= MENU[coffee_name]["ingredients"]["coffee"]


# TODO 1: Prompt user by asking, check input decide what to do next.
#  Also repeatable for the next customer.
while machine_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 3: Print report: When user enters "report", display the real-time resources.
    if user_input == "report":
        print(
            f"Water: {resources_update['water']}ml\nMilk: {resources_update['milk']}ml\n"
            f"Coffee: {resources_update['coffee']}ml\nMoney: ${resources_update['money']}\n")
        # TODO 2: Turn off the Coffee Machine by entering "off" to the prompt.
    elif user_input == "off":
        machine_is_on = False
    else:
        coffee_ingredients = MENU[user_input]["ingredients"]  # A dictionary
        coffee_cost = MENU[user_input]["cost"]  # float
        if is_enough_resource():
            # TODO 5: Process the coins if resources is enough, prompt customer to insert coins:
            print("Please insert coin.")
            quarters = int(input("how many quarters:"))
            dimes = int(input("how many dimes:"))
            nickles = int(input("how many nickles:"))
            pennies = int(input("how many pennies:"))
            user_paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            # TODO 6: Check the transaction successful?
            changes_amount = round((user_paid - coffee_cost), 2)
            if changes_amount >= 0:
                resources_update["money"] += coffee_cost
                if changes_amount > 0:
                    print(f"Here is your changes: ${changes_amount}")
                # TODO 7: Make the coffee, deduct the resources from report.
                make_coffee(user_input)
                # TODO 8: When the coffee is made, tell the user "Here is your [coffee]."
                print(f"Here is your {user_input}. Enjoy!")
            elif changes_amount < 0:
                print("Sorry, that's not enough money. Money refunded.")
