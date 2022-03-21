# given a val in an array remove all its intances in the given array.


def remove_intances(arr: list, value: int) -> list:
	return [val for val in arr if val != value]
			

def main():
	list = [7,7,7,2,5,7,8,7,4,3,6,4,3,7,9,7,7]
	list.sort()
	print(remove_intances(list, 7))

if __name__ == '__main__':
	main()
