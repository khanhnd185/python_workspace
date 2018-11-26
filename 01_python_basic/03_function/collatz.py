def collatz(number):
	if number % 2 == 0:
		return number // 2
	else:
		return 3*number+1
		
print('Enter an integer number:')
while True:
	try:
		num = int(input())
		break
	except ValueError:
		print('Not an integer. Try again')

step = 0
while True:
	num = collatz(num)
	print(num)
	step += 1
	if num == 1:
		break
		
print('Number turns to 1 after '+str(step)+' step(s)')