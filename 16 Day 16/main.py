from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

exit_program = False
while not exit_program:
    command = input(f"What would you like? ({menu.get_items()}): ")

    if command == "off":
        exit_program = True
    elif command == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
