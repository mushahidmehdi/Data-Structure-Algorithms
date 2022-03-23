# given an a set remove the element which occer twice and add the actual number at its position.


def remove_duplicate():

	lis = [1,2,3,4,3]
	result = []
	index = None
	for i in range(len(lis)):
		for j in range(len(lis)):
			if lis[i] == lis[j]:
				index = i
				break
	result.extend([index, index+1])
	return result

print(remove_duplicate())
