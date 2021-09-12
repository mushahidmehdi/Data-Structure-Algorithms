# In trapping rain water problem: we find the valley between two peaks to see how much the valley water could settle their.

# To Solve:
# We will create two arries given the peak arry; in first array we add the highest value traversing from left to right, & in second in right to left while adding the higest value.
# then by using the min out of both two new array and subtracting respective index from main array.

import unittest

def rain_water(arr):
	lr = list()
	temp = 0
	for i in arr:
		if temp < i:
			temp = i
		lr.append(temp)
	temp = 0
	rl = list()
	for i in reversed(arr):
		if temp < i:
			temp = i
		rl.append(temp)
	water_trap = 0
	for i in range(1, len(arr)-1):
		water_trap += (min(rl[i], lr[i]) - arr[i])
	return water_trap


class TestRain(unittest.TestCase):
	def test_rain_water(self):
		self.assertEqual(rain_water([7, 0, 4, 2, 5, 0, 6, 4, 0, 5]), 25)
		self.assertEqual(rain_water([12, 10, 6, 16, 8, 19]), 16)
		self.assertNotEqual(rain_water([7, 0, 0, 45, 61, 5]), 67)
		self.assertNotEqual(rain_water([7, 10, 4, 12, 12, 78]), 25)
		self.assertEqual(rain_water([]), 0)

if __name__ == '__main__':
	unittest.main()