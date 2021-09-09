# Bubble sort algorithm sort an array by comparing againt the element of the array by their prior neighbour and swap the position if the latter element is smaller compared to the prior element.

# Todos:
# open a while loop from second element of array till last.
# compare the second element with the first one.
# if latter is smaller than prior than swap the position.
# keep runnig the loop until all the elements has been exhausted.
import unittest
from unittest.result import failfast

def bubble_sort(arr):
	flag = True
	while flag:
		flag = False
		for i in range(1, len(arr)):
			if arr[i] < arr[i-1]:
				flag = True
				arr[i], arr[i-1]= arr[i-1], arr[i]
	return arr

arr3 = []
arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [4, 1, 3, 4, 6, 9, 10, 2, 0, 5]
arr4 = [100, 300, 900, 1000, 200, 400, 500, 700, 800]
arr1 = [12, 1087, 645, 235, 95, 534, 99, 736, 345]

class BubbleSort(unittest.TestCase):
	def test_bubble_sort(self):
		self.assertEqual(bubble_sort(arr3), [])
		self.assertEqual(bubble_sort(arr2), [0, 1, 2, 3, 4, 4, 5, 6, 9, 10])
		self.assertEqual(bubble_sort(arr5), [1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(bubble_sort(arr1), [12, 95, 99, 235, 345, 534, 645, 736, 1087])
		self.assertEqual(bubble_sort(arr4), [100, 200, 300, 400, 500, 700, 800, 900, 1000])

if __name__ == '__main__':
	unittest.main()

