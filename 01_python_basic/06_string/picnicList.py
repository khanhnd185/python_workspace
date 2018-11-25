def printPicnic(itemDict,leftWidth,rightWidth):
	print('PICNIC ITEMS'.center(leftWidth,'-'))
	for k,v in itemDict.items():
		print(k.ljust(leftWidth,'-')+str(v).rjust(rightWidth))
		
picnicItems = {'sandwich':4, 'apple':12, 'cup':4, 'cookies':8000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)