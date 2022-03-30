# given an array find whether we reach the last index or not by jumping by index valuing or =< 1 of the index value.

# To solve this problem we will using projectile movement with maximun jump with a reachability using valley idea.

# https://www.youtube.com/watch?v=muDPTDrpS28



def to_last_index(arr:list) -> bool:
	count = 0
	reachable = 0
	for i in range(len(arr)):
		if i > reachable:
			return False
		elif i + arr[i] > reachable:
			if i + arr[i] > len(arr):
				while i + arr[i] > len(arr):
					arr[i] -= 1
					reachable = i + arr[i]
				count += 1
			else:
				reachable = i + arr[i]
				print(reachable)		
				count += 1
	return reachable == len(arr)


def main():
	array = [1,1,4,1,2,0,1,1]
	print(to_last_index(array))

if __name__ == '__main__':
	main()
	
				
				

			


