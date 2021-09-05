# https://realpython.com/python-bitwise-operators/

# write a function which convert a decimal number into a binary number.

def deci_to_binary(number):
	# check if the number is less
	if number < 0:
		isNegative = True
		abs(number)
	else:
		isNegative = False

	result=''
	while number > 0:
		result = str(number%2) + result
		number = number//2
	if isNegative:
		result = '-' + result

	return result 
if __name__ == '__main__':
	binary = deci_to_binary(100)
	print(binary)

