import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumRegex = re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')

mo = phoneNumRegex.search('My number is 415-555-3434.')
print('Phone number found: '+mo.group())

#########
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 415-555-3434.')
print('Phone number found: '+mo.group(0))
print('Phone number found: '+mo.group(1))
print('Phone number found: '+mo.group(2))
print('Phone number found: '+mo.group())

print(mo.groups())
areaCode,mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 123-456-7890.')
print(mo1.group())
mo2 = phoneRegex.search('My number is 456-7890.')
print(mo2.group())
