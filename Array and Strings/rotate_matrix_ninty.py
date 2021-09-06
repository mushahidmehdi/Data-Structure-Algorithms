# given a matrix rotate it 90 degree to the left and right.


#import numpy as np
import unittest; import numpy as np

def rotate_ninty_left(mtrx):
	len_mtrx = len(mtrx)
	new_mtrx = [[0]*len_mtrx for i in range(len_mtrx)]
	for curr1, curr2 in zip(range(len_mtrx), range(len_mtrx-1, -1, -1)):
		for runer in range(len_mtrx):
			new_mtrx[curr1][runer] = mtrx[runer][curr2]
	return new_mtrx

def rotate_ninty_right(mtrx):
	len_mtrx = len(mtrx)
	new_mtrx = [[0]*len_mtrx for i in range(len_mtrx)]
	for cur1, cur2 in zip(range(len_mtrx), range(len_mtrx -1, -1, -1)):
		for run in range(len_mtrx):
			new_mtrx[run][cur1] = mtrx[cur2][run]
	return new_mtrx


class NintyDegreeRotation(unittest.TestCase):
	def test_right_rotation(self):
		self.assertEquals(rotate_ninty_right([[1, 2, 3],
											[4, 5, 6],
											[7, 8, 9]]),
											[[7, 4, 1],
											[8, 5, 2],
											[9, 6, 3],])
		self.assertEquals(rotate_ninty_right([[1, 2, 3, 4, 5],
											[6, 7, 8, 9, 10],
											[11, 12, 13, 14, 15],
											[16, 17, 18, 19, 20],
											[21, 22, 23, 24, 25]]),
											[[21, 16, 11, 6, 1],
											[22, 17, 12, 7, 2],
											[23, 18, 13, 8, 3],
											[24, 19, 14, 9, 4],
											[25, 20, 15, 10, 5]])
	def test_left_rotation(self):
		self.assertEqual(rotate_ninty_left([[1, 2, 3, 4, 5],
											[6, 7, 8, 9, 10],
											[11, 12, 13, 14, 15],
											[16, 17, 18, 19, 20],
											[21, 22, 23, 24, 25]]),
											[[5, 10, 15, 20, 25],
											[4, 9, 14, 19, 24],
											[3, 8, 13, 18, 23],
											[2, 7, 12, 17, 22],
											[1, 6, 11, 16, 21]])
		self.assertEquals(rotate_ninty_left([[1, 2, 3],
											[4, 5, 6],
											[7, 8, 9]]),
											[[3, 6, 9],
											[2, 5, 8],
											[1, 4, 7]])

if __name__ == '__main__':
	unittest.main()