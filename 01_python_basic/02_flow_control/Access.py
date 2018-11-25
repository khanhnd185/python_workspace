# Operators: == != > < <= >=
# Expression: and, or, not
# Blocks begin when the indentation increases
#

print('Input your name')
name = input()
print('Input your password')
password = input()
if name == 'Mary':
    print('Hello Mary')
    if password == 'sandwich':
        print('Access granted')
    else:
        print('Wrong password')
else:
    print('You cannot access')
