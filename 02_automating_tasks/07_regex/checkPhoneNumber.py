# Normal checking phone number with format xxx-xxx-xxxx
# isdecimal() is not available for python2
def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True
	

checkedString = '415-555-4242'
print(checkedString+' is a phone number: '+str(isPhoneNumber(checkedString)))
checkedString = '123-abc-2345'
print(checkedString+' is a phone number: '+str(isPhoneNumber(checkedString)))

message = 'Call me at 415-555-1011 tomorrow. 415-223-4456 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: '+chunk)
print('Done')