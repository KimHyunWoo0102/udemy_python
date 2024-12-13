from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()

coffeeMaker=CoffeeMaker()
moneyMachine=MoneyMachine()

isRun=True

while isRun :
# TODO : 1. Print what would you like? (espresso/latte/cappuccino)
    order=input("what would you like?("+menu.get_items()+") ")

    if order=='off':
        isRun=False
    elif order=='report':
        coffeeMaker.report()
    else :
        drink=menu.find_drink(order)
        moneyMachine.report()
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
            moneyMachine.report()

# TODO : 2. check the resources , we can make drink?
# TODO : 3. customer inputs there money