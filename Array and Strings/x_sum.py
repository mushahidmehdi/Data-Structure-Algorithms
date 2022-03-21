# X sum problem:  given a list find if there any sub array whose sum would be equal to some other number.
# this problem can be asked as 5-Sum, 4-Sum, 3-Sum, 2-Sum.



def two_sum(array: list, target: int) -> bool:
	hash_table = {}
	for index in range(len(array)):
		differ = target - array[index]
		if array[index] in hash_table:
			return [hash_table[array[index]], index]
		else:
			hash_table[differ] = index


def main():
	array =[12, 29, 10, 50, 433, 60, 67, 18]
	target = 30
	answer = two_sum(array, target)
	print(answer)


if __name__ == '__main__':
	main()