MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calculate_resources(resources, user_choice):
    if user_choice == "espresso":
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
    elif user_choice == "latte":
        resources["water"] = resources["water"] - 200
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 150
    else:
        resources["water"] = resources["water"] - 250
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 100

    return resources

money = 0

while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower().strip()

    if choice == "off":
        break

    if choice == "report":
        print(f"\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        continue
    else:
        if resources["water"] < MENU[choice]["ingredients"]["water"]:
            print("Sorry! There is not enough water.")
            continue

    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickels = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    change = total - MENU[choice]["cost"]


    if total >= MENU[choice]["cost"]:
        print(f"\nHere is ${change:.2f} in change.")
        print(f"here is your {choice} ☕️. Enjoy!")
        calculate_resources(resources, choice)
        money += MENU[choice]["cost"]
    else:
        print("Sorry. That's not enough money. Money refunded.")
