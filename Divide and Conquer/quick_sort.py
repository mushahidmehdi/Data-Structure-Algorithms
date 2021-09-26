# quick Sort is divide and conquer alghorithm.
# pick a random point (pivot) from the arry
# compared the rest of elemnet in array with pivot point and if the element is smaller than pivot append into left list, equal to middle list and greater to right list.

import random
import unittest

def quick_sort(arr):
	if len(arr) < 2:
		return arr
	
	left = []; middle=[]; right=[]
	pivot = arr[random.randint(0, len(arr)-1)]
	for i in arr:
		if i < pivot:
			left.append(i)
		elif i > pivot:
			right.append(i)
		else:
			middle.append(i)

	return quick_sort(left) + middle + quick_sort(right)


arr3 = []
arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [4, 1, 3, 4, 6, 9, 10, 2, 0, 5]
arr4 = [100, 300, 900, 1000, 200, 400, 500, 700, 800]
arr1 = [12, 1087, 645, 235, 95, 534, 99, 736, 345]

class MergeSort(unittest.TestCase):
	def test_quick_sort(self):
		self.assertEqual(quick_sort(arr3), [])
		self.assertEqual(quick_sort(arr2), [0, 1, 2, 3, 4, 4, 5, 6, 9, 10])
		self.assertEqual(quick_sort(arr5), [1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(quick_sort(arr1), [12, 95, 99, 235, 345, 534, 645, 736, 1087])
		self.assertEqual(quick_sort(arr4), [100, 200, 300, 400, 500, 700, 800, 900, 1000])

if __name__ == '__main__':
	unittest.main()