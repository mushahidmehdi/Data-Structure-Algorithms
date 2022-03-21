# given a list removed the duplicates.


def remove_duplicates(arr):
	return list(dict.fromkeys(arr))

def remove_elemets_sorted_arr(arr):
	counter = 0
	for i in range(len(arr) - 1):
		if arr[i] == arr[i + 1] :
			continue
		arr[counter] = arr[i]
		counter += 1
	return arr
		



def main():
	list = [2,5,7,8,4,3,6,4,3,7,9]
	list.sort()
	print(remove_duplicates(list))
	print(remove_elemets_sorted_arr(list))

if __name__ == '__main__':
	main()

