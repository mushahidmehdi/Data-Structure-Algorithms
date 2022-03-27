
# give the product of all other number in array except self


def product(arr:list)-> list:

	lr = [1 for i in range(len(arr))]
	rl = [1 for i in range(len(arr))]

	for i in range(1, len(arr)):
		lr[i] = arr[i-1] * lr[i-1]

	for i in range(1, len(arr)):
		rl[i] = arr[::-1][i-1] * rl[i-1]

	rl.reverse()

	for index, (i, j) in enumerate(zip(lr, rl)):
		rl[index] = i * j
	
	return rl




def main():
	array = [1,2,3,4]
	print(product(array))

if __name__ == '__main__':
	main()
