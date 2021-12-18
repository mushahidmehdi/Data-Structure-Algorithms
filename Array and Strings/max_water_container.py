# given a list of array find the max area between them, in other words find the area between two element in the array (if element consider the height) which range of elements can store the max water.


def max_area_between_two_arr(arr):
	"""this fuction will take quadartic time"""
	max_area = 0
	for index in range(len(arr)):
		for dist in range(index + 1, len(arr)):
			area = abs(index - dist) * min(arr[index], arr[dist])
			max_area = max(area, max_area)
	return max_area



def max_area_between_two_arr_optimized(arr):
	"""This function will take linear runtime"""
	start = 0 
	end = len(arr) -1
	max_area = 0

	while start < end:
		area = abs(end - start) * min(arr[end], arr[start])
		max_area = max(area,  max_area)

		if arr[start] < arr[end]:
			start += 1
		else:
			end -= 1
	return max_area


def main():
	list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
	print(max_area_between_two_arr(list))
	print(max_area_between_two_arr_optimized(list))

if __name__ == '__main__':
	main()
