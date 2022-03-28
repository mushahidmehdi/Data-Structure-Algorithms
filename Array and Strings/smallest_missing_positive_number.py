# Find the smallest positive number missing from an unsorted array

# To solve this problem we first sort all the array using merge_sort and then find the missing value

import unittest

def merge_sort(arr):
	length = len(arr)

	if length < 2:
		return arr
	
	mid = length // 2
	left = arr[:mid]
	right = arr[mid:]
	merge_sort(left)
	merge_sort(right)

	return merge_sort_util(left, right, arr)

def merge_sort_util(l, r, array):
	i = j = k = 0
	while i < len(l) and j < len(r):
		if l[i] < r[j]:
			array[i] = l[i]
			i += 1
		else:
			array[j] = r[j]
			j += 1
		k += 1
	
	while i < len(l):
		array[k] = l[i]
		i += 1
		k += 1
	while j < len(r):
		array[k] = r[j]
		j += 1
		k += 1

	return array 

def find_number(arr):
	merge_sort(arr)

	min_pos = 1

	while True:
		if min_pos not in arr:
			return min_pos
		min_pos += 1




class FindMinPositive(unittest.TestCase):

	def test_find_number(self):
		self.assertEqual(find_number([1,2,4,5,6,7]), 3)
		self.assertEqual(find_number([2,3,4,5]), 1)
		self.assertEqual(find_number([1,2,3,4,5,6,7]), 8)
		self.assertEqual(find_number([-1,0,1]), 2)
	
if __name__ == '__main__':
	unittest.main()
