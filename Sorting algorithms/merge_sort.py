# merge sort is an algorithm which used divide and conquer approuch;
# by recussively dividing into the arr into half on each recurssion, till divide no more. then comparing each element such a manner that the smaller append into a left list and greater into a riht list we build up the sorted arr.

# merge sort has time complexity of nlogn;

import unittest
def merge_sort(arr):
	if len(arr) < 2:
		return arr
	mid = len(arr)//2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left, right)

def merge(left, right):
	sorted = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sorted.append(left[i])
			i += 1
		else:
			sorted.append(right[j])
			j += 1
	
	while i < len(left):
		sorted.append(left[i])
		i += 1
	
	while j < len(right):
		sorted.append(right[j])
		j += 1

	return sorted

arr3 = []
arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [4, 1, 3, 4, 6, 9, 10, 2, 0, 5]
arr4 = [100, 300, 900, 1000, 200, 400, 500, 700, 800]
arr1 = [12, 1087, 645, 235, 95, 534, 99, 736, 345]

class MergeSort(unittest.TestCase):
	def test_merge_sort(self):
		self.assertEqual(merge_sort(arr3), [])
		self.assertEqual(merge_sort(arr2), [0, 1, 2, 3, 4, 4, 5, 6, 9, 10])
		self.assertEqual(merge_sort(arr5), [1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(merge_sort(arr1), [12, 95, 99, 235, 345, 534, 645, 736, 1087])
		self.assertEqual(merge_sort(arr4), [100, 200, 300, 400, 500, 700, 800, 900, 1000])

if __name__ == '__main__':
	unittest.main()