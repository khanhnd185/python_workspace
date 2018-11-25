def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argumet')

print(spam(2))
print(spam(7))
print(spam(0))
