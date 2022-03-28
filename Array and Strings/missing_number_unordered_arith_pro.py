# We will use XOR operatore to find the missing number in unordered Arithmetic Progression

def missing_one(arr):
	xor = 0
	commen_diff = (max(arr) - min(arr)) // len(arr)

	for i in range(len(arr)):
		xor = xor ^ arr[i]

	for i in range(len(arr)+1):
		xor = xor ^ (min(arr) + (i * commen_diff))
	
	return xor

def main():
	arr = [2,6,8,10,12]
	print(missing_one(arr))

if __name__ == '__main__':
	main()
