from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

while True:
    choice = input(f"\nWhat would you like? (espresso/latte/cappuccino): ").lower().strip()

    if choice == "off":
        break

    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
        continue
    else:
        drink = menu.find_drink(choice)
        can_make = coffeeMaker.is_resource_sufficient(drink)
        if can_make:
            if moneyMachine.make_payment(drink.cost):
                moneyMachine.report()
                coffeeMaker.make_coffee(drink)
        else:
            continue