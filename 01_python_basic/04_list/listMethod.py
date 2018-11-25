a = [1,2,3]
b = ['cat','bat','rat','elephant']
c = ['hello',3.1415,True,None,42]
d = [['cat','bat'],[10,20,30,40,50]]
print(len(a))
print(len(b))
print(len(c))
print(len(d))


b[1] = b[2]
print(b)
b[1] = 'monkey'
print(b)

print(a+b)
print(c+d)
print(len(c+d))

e = b
print(e)
del e[1]
print(e)
print(b)


print('howdy' in ['hello','howdy','hi','heya'])
print('cat' in ['hello','howdy','hi','heya'])

myPets = ['Poo','Po','Pi']
print('Enter a pet name:')
namePet = input()
if namePet not in myPets:
    print('I do not have a pet named '+ namePet)
else:
    print(namePet + ' is my pet.')

cat = ['fat','black','loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
name = 'Poo'
[size, color, disposition] = cat
print(cat)
# size, color, disposition, name = cat
print(cat)

print(b)
print(b.index('cat'))
b.append('ant')
print(b)
print(e)
b.insert(2,'bear')
print(b)
print(e)
b.append('cat')
b.remove('ant')
b.remove('cat')
print(b)
print(e)

numList = [-7, 1, 2,-3, 0.123]
numList.sort()
print(numList)
b.sort()
print(b)
b.sort(reverse=True)
print(b)
b.append('Elephant')
print(b)
b.sort()
print(b)
b.sort(key=str.lower)
print(b)
