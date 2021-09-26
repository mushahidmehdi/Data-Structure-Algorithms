# given a list of array find the max area between them, in other word find the area between two element in the array (if element consider the height) which range of element can store the max water.

def brute_force(container):
	"""This solution comes up with square of length of arr"""
	max_area = 0
	for l in range(len(container)):
		for r in range(l+1, len(container)):
			area = abs(l-r) * min(container[r], container[l])
			max_area = max(max_area, area)
	return max_area

def optimal(container):
	"""if we move the smaller heigth toward the greater height we can decrease runtime by O(n)"""
	maxContainer = 0
	left, right = 0, len(container) -1 # len beggin with 1 & list index beggin 0
	while left < right:
		area = abs(left - right) * min(container[left], container[right])
		maxContainer = max(area, maxContainer)

		if container[left] < container[right]:
			left += 1
		else:
			right -= 1
	return maxContainer

def main():
	list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
	list = [23, -1, 84 ,36, 2, - 5, 0, 3,7]
	print(brute_force(list))
	print(optimal(list))

if __name__ == '__main__':
	main()

		