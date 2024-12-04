def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for i, j in inventory.items():
        print( str(j) + ' ' + i)
        total = total + inventory.get(i, 0)
    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for i, j in enumerate(addedItems):
        inventory[j] = inventory.get(j, 0) + 1
    displayInventory(inventory)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
