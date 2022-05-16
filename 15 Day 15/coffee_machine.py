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
    "money": 0,
}


def report():
    resource = 0
    for key, value in resources.items():
        print(f"{key.capitalize()}: {value}{['ml', 'ml', 'g', '$'][resource]}")
        resource += 1


def is_enough_resources(coffee_type):
    for key, value in MENU[coffee_type]["ingredients"].items():
        if value >= resources[key]:
            return key
    return False


def make_coffee(coffee_type):
    for key, value in MENU[coffee_type]["ingredients"].items():
        resources[key] -= value
    print(f"Here is your {command} ☕. Enjoy!")


def insert():
    insert_amount = 0
    insert_amount += float(input("How many quarters?: ")) * 0.25
    insert_amount += float(input("How many dimes?: ")) * 0.10
    insert_amount += float(input("How many nickles?: ")) * 0.05
    insert_amount += float(input("How many pennies?: ")) * 0.01
    return insert_amount


exit_program = False
while not exit_program:
    command = input("What would you like? (espresso/latte/cappuccino): ")

    if command == 'off':
        exit_program = True
    elif command == 'report':
        report()
    elif command in ['espresso', 'latte', 'cappuccino']:
        missing_resource = is_enough_resources(command)
        if not missing_resource:
            cost = MENU[command]["cost"]
            print("Please insert coins.")
            total_insert = insert()
            if total_insert >= cost:
                resources["money"] += cost
                if total_insert > cost:
                    print(f"Here is ${round(total_insert - cost, 2)} in change.")
                make_coffee(command)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {missing_resource}.")



