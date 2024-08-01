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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    payment = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.5 + pennies * 0.01)
    return payment


def is_payment_sufficient(payment, order_cost):
    if payment >= order_cost:
        global money
        money += payment
        change = round(payment - order_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print(f"Sorry, there is not enough money. Money refunded.")
        return False


def make_coffee(order, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order}. Enjoy it!")


is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nProfit: "
              f"${money}")
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = insert_coins()
            if is_payment_sufficient(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])


