import random

print('I am thinking of a number between 1 and 20')
result = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess')
    guessNumber = int(input())

    if (guessNumber > result):
        print('You guess too high')
    elif (guessNumber < result):
        print('You guess too low')
    else:
        break

if (guessNumber == result):
    print('Correct!!')
else:
    print('Gamev over!!')
print('My number is ',result)
