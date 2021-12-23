from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_input = (input(f"What would you like? (espresso/latte/cappuccino): "))
machine_is_on = True
coffeeMaker_obj = CoffeeMaker()
moneyMachine_obj = MoneyMachine()
menu_obj = Menu()
while machine_is_on:
    if user_input == "report":
        coffeeMaker_obj.report()
        moneyMachine_obj.report()
    elif user_input == "off":
        machine_is_on = False
        break
    else:
        order_item = menu_obj.find_drink(user_input)
        if coffeeMaker_obj.is_resource_sufficient(order_item):
            if moneyMachine_obj.make_payment(order_item.cost):
                coffeeMaker_obj.make_coffee(order_item)
    user_input = (input(f"What would you like? (espresso/latte/cappuccino): "))

