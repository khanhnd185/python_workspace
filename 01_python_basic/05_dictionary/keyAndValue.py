spam = {'color':'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

print(spam.keys())
print(list(spam.keys()))

print(type(spam.values()))
print(type(spam.keys()))
print(type(spam.items()))

for k,v in spam.items():
    print('Key: '+k+' Value: '+str(v))
    
'color' in spam.keys()
'red' in spam.values()
'name' not in spam.keys()
'Kay' not in spam.values()

picnicItems = {'apple': 5, 'cup':2}
print('I am bringing '+str(picnicItems.get('cup',0))+ ' cups')
print('I am bringing '+str(picnicItems.get('egg',0))+ ' eggs')
picnicItems['apple'] = 4
print('I am bringing '+str(picnicItems.get('apple',0))+ ' apples')
# print('I am bringing '+str(picnicItems['egg'])+ ' eggs')

picnicItems.setdefault('eggs',4)
picnicItems.setdefault('eggs',2)
