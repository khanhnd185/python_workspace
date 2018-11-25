spam = 'Hello world'
spam[0]
spam[4]
spam[-1]
spam[0:5]
spam[:5]
spam[6:]
'Hello' in spam
'Hi' not in spam
fizz = spam[0:5]

spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

'Hello'.islower()
'HELLO'.islower()
'hello'.islower()

'Hello'.isupper()
'HELLO'.isupper()
'hello'.isupper()

'123'.islower()
'123'.isupper()

'123abc'.islower()
'123abc'.isupper()
