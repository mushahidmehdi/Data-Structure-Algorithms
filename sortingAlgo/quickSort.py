import random 
from selectionSort import numList

def quick_sort(list):
	if len(list) < 2:
		return list
	pivot = list[random.randint(0, len(list)-1)]
	bigger, smaller, equal = [], [], []

	for i in list:
		if i < pivot:
			smaller.append(i)
		elif i > pivot:
			bigger.append(i)
		else:
			equal.append(i)

	return quick_sort(smaller) + equal + quick_sort(bigger)

print(quick_sort(numList))

#	list1 = [1,2,3]
#	list2 = [4,5,6]
#	
#	print(list1 + list2)