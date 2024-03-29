from file_resource import MENU, resources


def report_machine(machine_resource):
    print("Machine Coffee Report")
    list_item = [ ['',   '',   '',  '$'],
                  ['ml', 'ml', 'g', '' ]]
    k = 0
    for key, values in machine_resource.items():
        print(f"  {key.title()}: {list_item[0][k]}{values}{list_item[1][k]}")
        k += 1

def check_resources_insufficient(machine_resource, name_coffee):
    dict_drink = MENU[name_coffee]["ingredients"]

    for key, values in dict_drink.items():
        if (machine_resource[key] - values) < 0:
            print(f"“Sorry there is not enough {key}.")
            return True
    return False

def check_and_receive_money(name_coffee):
    money_need = MENU[name_coffee]["cost"]

    print(f"Please insert ${money_need}:")
    list_money_value = [0.25, 0.10, 0.05, 0.01]
    list_money_types = ["quartes", "dimes", "nickles", "pennies"]
    total_insert = 0
    for i in range(len(list_money_types)):
        inserted = int(input(f"How many {list_money_types[i]}(${list_money_value[i]})? "))
        total_insert += inserted*list_money_value[i]

    if total_insert < money_need:
        print("Sorry that's not enough money. Money refunded.")
        return -1

    if total_insert > money_need:
        change = round(total_insert - money_need, 2)
        print(f"Here is ${change} dollars in change.")
    return money_need


def make_coffee(machine_resource, name_coffee):
    dict_coffee = MENU[name_coffee]["ingredients"]
    for key, values in dict_coffee.items():
        machine_resource[key] -= values
    print(f"Here is your {name_coffee}. Enjoy!")


def produce_coffee(machine_resource, name_coffee):
    if check_resources_insufficient(machine_resource, name_coffee):
        return False

    money_inserted = check_and_receive_money(name_coffee)
    if money_inserted == -1:
        return False

    machine_resource['money'] += money_inserted
    print(f"The machine have ${machine_resource['money']} to future buy.")
    make_coffee(machine_resource, name_coffee)
    return True


def start_machine():
    is_machine_working = True
    machine_resource = resources
    machine_resource['money'] = 0

    while is_machine_working:
        answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if answer == "off":
            is_machine_working = False
        elif answer == "report":
            report_machine(machine_resource)
        elif answer in ['espresso', 'latte', 'cappuccino']:
            produce_coffee(machine_resource, answer)
        else:
            print("Command no exist in this machine")


start_machine()
