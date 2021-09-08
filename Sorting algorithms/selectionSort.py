# Selection sort is an array sorting algorithem which sort given array by picking each element in the array and comparing againt the rest of element in the array.

# to solve this algorithem we can used runner technique; where by initialting two loop one inside the other and by compaing curr itter of outter loop with complete itteration if inner loop; and if current itteration of exteranal loop is smaller any itteration of inner loop we will swap their postion.

import unittest

def selection_sort(arr):
	curIndex = 0
	while curIndex < len(arr):
		for i in range(len(arr)):
			if arr[curIndex] < arr[i]:
				arr[curIndex], arr[i] = arr[i], arr[curIndex]
		curIndex += 1
	return arr


arr3 = []
arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [4, 1, 3, 4, 6, 9, 10, 2, 0, 5]
arr4 = [100, 300, 900, 1000, 200, 400, 500, 700, 800]
arr1 = [12, 1087, 645, 235, 95, 534, 99, 736, 345]

class SelectionSort(unittest.TestCase):
	def test_selection_sort(self):
		self.assertEqual(selection_sort(arr3), [])
		self.assertEqual(selection_sort(arr2), [0, 1, 2, 3, 4, 4, 5, 6, 9, 10])
		self.assertEqual(selection_sort(arr5), [1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(selection_sort(arr1), [12, 95, 99, 235, 345, 534, 645, 736, 1087])
		self.assertEqual(selection_sort(arr4), [100, 200, 300, 400, 500, 700, 800, 900, 1000])

if __name__ == '__main__':
	unittest.main()
# the time complexity of this algorithem is N*N where N is len of array;
# because there are two traversals.

