def printTable(table):
	longestWord = []
	for col in range(0,len(table)):
		longestWord += [len(table[col][0])]
		# longestWord[col] = len(table[col][0])
		for row in range(0,len(table[1])):
			if longestWord[col] < len(table[col][row]):
				longestWord[col] = len(table[col][row])
	
	for row in range(0,len(table[0])):
		for col in range(0,len(table)):
			print(table[col][row].rjust(longestWord[col]),end=' ')
		print('\n')
		
	
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
print(len(tableData))
print(len(tableData[0]))
printTable(tableData)