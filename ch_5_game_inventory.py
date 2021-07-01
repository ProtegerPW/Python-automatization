def displayInventory(dictArg):
    totalNumOfItems = 0
    print("Inventory")
    for k, v in dictArg.items():
        print (str(v) + " " + k)
        totalNumOfItems += v
    
    print("Total number of items: " + str(totalNumOfItems))


if __name__ == '__main__':
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    displayInventory(stuff)
    