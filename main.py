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


def profit():
    flag = False
    while not flag:
        ask = input("What would you like? (espresso/latte/cappuccino):")
        if ask == "report":
            print(f'water: {resources["water"]}ml')
            print(f'milk: {resources["milk"]}ml')
            print(f'coffee: {resources["coffee"]}g')
        elif resources["water"] < MENU[ask]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            profit()
        if ask == "espresso" or ask == "latte" or ask == "cappuccino":

            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            input_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            input_money = round(input_money, 2)
            cost_menu = MENU[ask]["cost"]

            if ask == "espresso":
                if cost_menu > input_money:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    charge = input_money - cost_menu
                    charge = round(charge, 2)
                    print(f"Here is {charge} in change.")
                    print(f"Here is your {ask}. Enjoy!")
                    resources["water"] = resources["water"] - MENU[ask]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU[ask]["ingredients"]["coffee"]

            elif ask == "latte":
                if cost_menu > input_money:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    charge = input_money - cost_menu
                    charge = round(charge, 2)
                    print(f"Here is {charge} in change.")
                    print(f"Here is your {ask}. Enjoy!")
                    resources["water"] = resources["water"] - MENU[ask]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - MENU[ask]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - MENU[ask]["ingredients"]["coffee"]

            elif ask == "cappuccino":
                if cost_menu > input_money:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    charge = input_money - cost_menu
                    charge = round(charge, 2)
                    print(f"Here is {charge} in change.")
                    print(f"Here is your {ask}. Enjoy!")
                    resources["water"] = resources["water"] - MENU[ask]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - MENU[ask]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - MENU[ask]["ingredients"]["coffee"]


profit()


