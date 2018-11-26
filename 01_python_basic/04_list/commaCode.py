def commaCode(stringList):
	length = len(stringList)
	if length == 0:
		return ""
	elif length == 1:
		return str(stringList[0])
	else:
		string = stringList[0]
		for j in range(1,length-1):
			string = string + ', ' + str(stringList[j])
		string = string+ ' and '+str(stringList[length-1])
		return string


spam = ['apples','bananas','tofu','cats',4.3]		
print(commaCode([]))
print(commaCode(spam[:1]))
print(commaCode(spam[:2]))
print(commaCode(spam[:3]))
print(commaCode(spam[:4]))
print(commaCode(spam[:5]))