while True:
    print('Enter your username:')
    user = input()
    if user.isalpha():
        break
    print('Please enter characters only')

while True:
    print('Enter your password:')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers.')

