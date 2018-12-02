import re
heroRegex = re.compile(r'Batman|Captain')
mo1 = heroRegex.search('Batman and Captain')
print(mo1.group())
mo2 = heroRegex.search('Captain and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# Matching zero or one with ?
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3 == None)


# Matching zero or more with *
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())


# Matching one or more with +
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1 == None)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())

# Matching with specific repetitions with {}
# (Ha){3} = (Ha)(Ha)(Ha)
# (Ha){3,5} = ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
# (Ha){,3} = ()|(Ha)|((Ha)(Ha))|((Ha)(Ha)(Ha))
# (Ha){3,} = ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))|...
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('HaHa')
print(mo2 == None)



