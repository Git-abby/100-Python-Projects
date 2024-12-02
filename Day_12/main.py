from data import MENU, resources


#TODO 1
'''Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.'''

profit = 0
is_machine_on = True

def check_resources_suffieciency(drink, resources):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"❓ Sorry there is not enough {item}.")
            return False
    return True

def check_coins():
    print("Please insert coins.💲")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def check_successful_transaction(drink_cost, money_received):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("❓ Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2 "Turn off the Coffee Machine by entering “ off ” to the prompt."
    if choice == 'off':
        is_machine_on = False
    # TODO 3 "Print report. - generated that shows the current resource values"
    elif choice == 'report':
        current_resources = resources
        print(f"the current resource values.\n\t🔵Water: {resources['water']}ml\n\t⚪️Milk: {resources['milk']}ml\n\t🟤Coffee: {resources['coffee']}g\n\t🟢Money: 💲{profit}")
    else:
        drink = MENU[choice]
        #TODO 4 "Check resources sufficient?"
        if check_resources_suffieciency(drink['ingredients'], resources):
            # TODO 5 Process coins.
            payment = check_coins()
            if check_successful_transaction(drink['cost'], payment):
                make_coffee(choice, drink['ingredients'])
