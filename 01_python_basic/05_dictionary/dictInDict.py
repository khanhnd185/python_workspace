allGuest = {'Alice': {'apples':5, 'pretzels':12},
            'Bob': {'sandwiches':3, 'apples':2,},
            'Carol': {'cups':3, 'pies':1}}

def totalBrought(guest,item):
    numBrought = 0
    for k,v in guest.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Number of things being brought:')

print('- Apples     '+str(totalBrought(allGuest,'apple')))
print('- sandwiches '+str(totalBrought(allGuest,'sandwiches')))
print('- pretzels   '+str(totalBrought(allGuest,'apple')))
print('- cups       '+str(totalBrought(allGuest,'apple')))
print('- pies       '+str(totalBrought(allGuest,'apple')))
