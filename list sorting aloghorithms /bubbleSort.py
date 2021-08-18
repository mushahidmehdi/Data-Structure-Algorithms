from array import array
from math import fabs
from mergeSort import numList

def bubble_sort(arr):
	flag = False
	while not flag:
		flag = True
		for i in range(1, len(arr)):
			if arr[i] < arr[i-1]:
				flag = False
				arr[i], arr[i-1] = arr[i-1], arr[i]
			
	return arr


print()
print('numList with order' + str(bubble_sort(numList)))

