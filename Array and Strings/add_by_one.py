# given a list of integers add one into the list 

import unittest

def add_one(arr: list):
	temp = []
	if len(arr) == 0:
		temp.append(1)
		return temp
	carry = 1

	for idx in range(len(arr) -1 , -1, -1):
		if arr[idx] == 9:
			arr[idx] = 0
		else:
			carry += arr[idx] 
			arr[idx] = carry
			break
	if arr[0] == 0:
		arr.insert(0, 1)
		return arr
		
	return arr



class AddOne(unittest.TestCase):
	def test_add_one(self):
		self.assertEqual(add_one([2,5,6,7]), [2,5,6,8])
		self.assertEqual(add_one([8,8,9,9]), [8,9,0,0])
		self.assertEqual(add_one([9,9,9,9,9]), [1,0,0,0,0,0])
		self.assertEqual(add_one([1,2,2,1,1]), [1,2,2,1,2])
		self.assertEqual(add_one([9,9,9,9,1]), [9,9,9,9,2])
		self.assertEqual(add_one([]), [1])

if __name__ == '__main__':
	unittest.main()