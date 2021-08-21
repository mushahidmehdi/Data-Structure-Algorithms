numList = [12, 23, 16, 69, 3, 78, 56, 45, 54, 65, 85, 15, 19, 91]

def selection_sort(arr):
	indexPosition = 0
	while len(arr) > indexPosition:
		for i in range(len(arr)):
			if arr[indexPosition] < arr[i]:
				arr[indexPosition], arr[i] = arr[i], arr[indexPosition]
		indexPosition += 1
	return arr

print()
print("original arr " + str(numList))
print()
print("sorted array " + str(selection_sort(numList)))
print()