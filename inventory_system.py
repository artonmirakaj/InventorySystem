
inventory = {"apples": 5, "oranges": 10, "bananas": 4, "kiwi": 6}
check = 1

def buy(type, quantity):
    if type in inventory:
        inventory[type] = inventory[type] + quantity
    else:
        print "not in inventory"


def sell(type, quantity):
    if type in inventory:
        inventory[type] = inventory[type] - quantity
    else:
        print "not in inventory"


def report(type=""):
    if type:
        if type in inventory:
            print str(inventory[type])
        else:
            print "not in inventory"

    else:
        print str(inventory)


while check != 0:

    prompt = int(raw_input("Enter '1' stock: "
                           "Enter '2' sell: "
                           "Enter '3' report: "
                           "Enter '0' to quit\n"))

    if prompt == 1:
        fruit = raw_input("fruit: ")
        num = int(raw_input("quantity: "))
        buy(fruit, num)

    elif prompt == 2:
        fruit = raw_input("fruit: ")
        num = int(raw_input("quantity: "))
        sell(fruit, num)

    elif prompt == 3:
        selection = raw_input("Enter fruit name if you want to check one fruit, hit enter key if you want all fruit amounts:\n")

        if selection:
            report(selection)
        else:
            report()

    elif prompt == 0:
        exit()
