import copy
aList = list('hello')
aCopyList = copy.copy(aList)
aCopyList[0] = 'b'
print(aList)
print(aCopyList)
