spam = '       Hello world    '
print(spam.strip())
print(spam.rstrip())
print(spam.lstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# spam.strip('mapS')
# spam.strip('Spam')