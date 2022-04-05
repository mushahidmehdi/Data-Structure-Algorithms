#  Write a decorator in python that will count how many times the decorated function was called. It should print the number every time the decorated function is executed. Each function should be counted separately.





def decor(func):
	def helper(x):
		helper.get_call += 1
		newfun = func(x)
		return newfun
	# as python function is an object we created an 
	# attibute for the helper function
	helper.get_call = 1
	return helper

@decor
def perfect_sqre(x):
	# perfect square of number range 1 to 5
	perfect_sqre = x * x
	return perfect_sqre

def main():
	for num in range(5):
		if perfect_sqre.get_call == 1:
			# we are able to access the get_call in p
			# erfect_sqre because the helper function 
			# is adding a new functionatiy to perfect_sqre function
			print(f'helper function called', perfect_sqre.get_call,  '\'st time')
		else:
			print('helper function called', perfect_sqre.get_call,  'times')	

		print(f'perfect square of {num} is {perfect_sqre(num)}')

if __name__ == '__main__':
	main()