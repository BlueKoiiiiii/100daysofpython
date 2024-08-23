import menu
from menu import Menu, MenuItem
from cofee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = menu.Menu()
programend = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while not programend:
    prompt = input(f"What would you like?({menu.get_items()})\n").lower()

    if prompt == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif prompt == "stop":
        programend = True
    else:
        item = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)

