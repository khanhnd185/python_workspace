def spam():
    eggs = 199
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(str(ham) + ' ' + str(eggs))

spam()

# This will cause error because variable eggs is a local variable
# print(eggs)
