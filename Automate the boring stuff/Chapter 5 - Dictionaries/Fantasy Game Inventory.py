inventory = {"Rope": 1, "Torch": 6, "Gold Coin": 42, "Dagger": 1, "Arrow": 12}

def displayinventory(inventory):

    print("Inventory:")
    totalinv = 0

    for items in inventory.items():
        print(items[1], items[0])
        totalinv += int(items[1])

    print ("\nTotal Inventory:" + str(totalinv))

displayinventory(inventory)
