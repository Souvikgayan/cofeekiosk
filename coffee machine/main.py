import os
from art import logo as LOGO
from data import MENU, resources



def show_report():
    """It prints the available ingridients of the coffee machine and collected money"""
    print(f"Water: {WATER} ml")
    print(f"Milk: {MILK} ml")
    print(f"Coffee: {COFFEE} gm")
    print(f"Money: ₹{MONEY}")


def is_available(order):
    """It takes a 'customer order' as input and returns 'True' or 'False' according to 'availablity of ingredients' in the coffee machine"""
    required_water = MENU[order]['ingredients']['water']
    required_milk = MENU[order]['ingredients']['milk']
    required_coffee = MENU[order]['ingredients']['coffee']

    if required_water <= WATER and required_milk <= MILK and required_coffee <= COFFEE:
        return True
    else:
        return False
    

def payment_success(order):
    """It takes a 'customer order' as input and returns two output, 'True' or 'False' according to successfull payment and the amount of money paid by customer"""
    actual_cost = MENU[order]['cost']
    coin_10 = float(input("How many ₹10: ")) * 10
    coin_5 = float(input("How many ₹5: ")) * 5
    coin_2 = float(input("How many ₹2: ")) * 2
    coin_1 = float(input("How many ₹1: ")) * 1

    user_payment = coin_10 + coin_5 + coin_2 + coin_1
    print("\n")

    if user_payment == actual_cost:
        return True, actual_cost
    elif user_payment > actual_cost:
        print(f"Please collect ₹{user_payment-actual_cost} in change")
        return True, actual_cost
    else:
        return False, 0
    

def ingredients_left(order):
    """It takes a 'customer order' and returns 'how much ingredients used in that order'"""
    water = MENU[order]['ingredients']['water']
    milk = MENU[order]['ingredients']['milk']
    coffee = MENU[order]['ingredients']['coffee']

    water = WATER - water
    milk = MILK - milk
    coffee = COFFEE - coffee
    return water, milk, coffee



###----Starting of the main coffee machine code----###

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0

machine_on = True

while machine_on:
    print(LOGO)
    customer_choice = input("What would you like? (Espresso/Latte/Cappucino): ").lower()

    if customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":

        if is_available(customer_choice):
            cost = MENU[customer_choice]['cost']
            print(f"Your bill ₹{cost}\nPlease insert coins.\n")
            result, money = payment_success(customer_choice)
            MONEY += money

            if result:
                print(f"Here is your {customer_choice.title()}☕. Enjoy!")
                WATER, MILK, COFFEE = ingredients_left(customer_choice)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry we have no sufficiant ingredients.")

    elif customer_choice == "report":
        show_report()

    elif customer_choice == "off":
        machine_on = False

    elif customer_choice == "money":
        print(f"We have ₹{MONEY}")

    else:
        print("Please enter right order.")
