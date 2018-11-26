def displayInventory(inventoryDict):
	print('Inventory:')
	total = 0
	for k,v in inventoryDict.items():
		print(str(v)+' '+k)
		total += v
	print('Total number of items: '+str(total))
	
def addToInventory(inventory, addedItems):
	for item in addedItems:
		inventory.setdefault(item,0)
		inventory[item] += 1

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
displayInventory(stuff)

dragonLoot = ['gold coin','dagger','gold coin','ruby']
addToInventory(stuff,dragonLoot)
displayInventory(stuff)