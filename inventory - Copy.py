def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for i, j in inventory.items():
        print( str(j) + ' ' + i)
        total = total + inventory.get(i, 0)
    print('Total number of items: ' + str(total))

a = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1,'arrow': 12}
displayInventory(a)
