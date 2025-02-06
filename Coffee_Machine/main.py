from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker_ = CoffeeMaker()
money_machine_ = MoneyMachine()

menu_items = menu.get_items()

operating = True

while operating:
    user_input = input(f"What would you like? ({menu_items}): ").lower()

    if user_input == "off":
        operating = False
    elif user_input == "report":
        coffe_maker_.report()
        money_machine_.report()
    elif user_input in menu_items.split("/"):
        drink = menu.find_drink(user_input)
        if coffe_maker_.is_resource_sufficient(drink):
            print(f"The coffee costs ${drink.cost}")
            money_machine_.make_payment(drink.cost)
            coffe_maker_.make_coffee(drink)
    else:
        print("Please enter a valid input")