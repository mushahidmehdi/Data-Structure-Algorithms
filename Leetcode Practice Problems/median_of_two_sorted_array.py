# given two sorted arr find median to merged of both sorted arr..
# https://atharayil.medium.com/median-of-two-sorted-arrays-day-36-python-fcbd2dbbb668

import math

def brute_force(arr1, arr2):
	outputList = []
	# traversing through all arr1 and arr2 until == empty one of them
	while (arr1 and arr2):
		if arr1[0] < arr2[0]:
			outputList.append(arr1.pop(0))
		else:
			outputList.append(arr2.pop(0))
	while arr1:
		outputList.append(arr1.pop(0))
	while arr2:
		outputList.append(arr2.pop(0))
	mid = len(outputList) // 2
	print(outputList)
	if len(outputList) % 2 == 0:
		return float((outputList[mid-1]+outputList[mid]) / 2)
	return outputList[mid]


def main():
	arr1 = [5,5,6,7]	
	arr2 = [3, 4, 6]
	print(brute_force(arr1, arr2))

if __name__ == '__main__':
	main()