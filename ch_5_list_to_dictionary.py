def addToInventory(inventory, newItems):
    for item in newItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1


def displayInventory(dictArg):
    totalNumOfItems = 0
    print("Inventory")
    for k, v in dictArg.items():
        print (str(v) + " " + k)
        totalNumOfItems += v
    
    print("Total number of items: " + str(totalNumOfItems))


if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    addToInventory(inv, dragonLoot)
    displayInventory(inv)