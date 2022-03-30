

# given a query with starting and ending Index with a value to add between between them, find the greatest value that can be create using these quries.

# https://www.youtube.com/watch?v=EnxYdFQpAMU

# start, end,  value
#   1,    2,   100
#   2,    5,   100   ----> [0, 100, 200, 200, 200, 100] ----> 200
#   3,    4,   100

# we will create a new array of length n + 2
# we will add the value at the start but add negative value at the end+1 index of the new array 
# then we sum up from left to right of the array and retuen the maximun.

def array_manipulation(array:list, n:int):
	arr = [0] * (n + 2)

	for query in range(1, len(array)):
		start = array[query][0]
		end = array[query][1]
		value = array[query][2]
	
		arr[start] = arr[start] + value
		arr[end+1] = arr[end+1] -value
		
	for i in range(1, len(arr)):
		arr[i] = arr[i-1] + arr[i] 
		
	return max(arr)

def main():
	matrix = [[1,2,100], [2,5,100], [3,4,100]]
	n = 5
	print(array_manipulation(matrix, n))

if __name__ == '__main__':
	main()