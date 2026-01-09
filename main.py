MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coins={'quarters':0.25, 'dimes':0.10, 'nickels':0.05, 'pennies':0.01}
def off():
    print("TURN OFF")
def report():
    for item in resources:
        print(f"{item} : {resources[item]}")
    print(f"money : {profit}")
def payment():
    global profit
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coffee_cost = MENU[customer_choice]["cost"]
    total_amount = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    if total_amount >= coffee_cost:
        change = total_amount - coffee_cost
        print(f"Here is {round(change,2)} in change.")
        print("Here is your espresso ☕️. Enjoy!")
        profit += coffee_cost
        for item in resources:
            for item1 in MENU[customer_choice]["ingredients"]:
                if item == item1:
                    resources[item] -= MENU[customer_choice]["ingredients"][item]
        return coffee_cost
    else:
        print("Sorry that's not enough money. Money refunded.")

def check_resources():
    for item in resources:
        for item1 in MENU[customer_choice]["ingredients"]:
            if resources[item] < MENU[customer_choice]["ingredients"][item]:
                print(f"Sorry, there is not enough {item}.")
                return
    return payment()
repeat= True
while repeat:
    customer_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if customer_choice == "off":
        off()
        repeat = False
    elif customer_choice == "report":
        report()
    else:
        check_resources()