
# Given a list replace all the zero at the begging of the list inplace.

import unittest


def move_zero(arr: list) -> list:

	curr_idx = len(arr) -1
	change_idx = len(arr) -1

	while curr_idx >= 0:
		if arr[curr_idx] != 0:
			arr[change_idx] = arr[curr_idx]
			change_idx -= 1

		curr_idx -= 1

	while change_idx >= 0:
		arr[change_idx] = 0
		change_idx -= 1

	return arr

class MoveZero(unittest.TestCase):
	def test_move_zero(self):
		self.assertEqual(move_zero([2,5,0,7,9,0]), [0,0,2,5,7,9])
		self.assertEqual(move_zero([21,51,10,17,19,0]), [0,21,51,10,17,19])
		self.assertEqual(move_zero([99,202,0,10,1]), [0,99,202,10,1])
		self.assertEqual(move_zero([0,0,1]), [0,0,1])
		self.assertEqual(move_zero([]), [])


if __name__ == '__main__':
	unittest.main()
	