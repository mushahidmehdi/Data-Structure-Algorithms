# Building a binary search tree from sorted array:


# method:
# we will find the middle node of sorted array and make it root of the tree and then find the middle note of right half and left half and make them root of right and left side of branch respectively, using recussion;


class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

	
def balanced_bst_from_sorted_array(arr):
	if not arr: return
	mid = (len(arr))//2
	root = Node(arr[mid])
	root.left = balanced_bst_from_sorted_array(arr[:mid])
	root.right = balanced_bst_from_sorted_array(arr[mid+1:])
	return root

def pre_order(node):
	if not node: return
	print(node.data, end=' ')
	pre_order(node.left)
	pre_order(node.right)

if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8,9] # ans 5 3 2 1 4 8 7 6 9 
	arr = [1, 2, 3, 4, 5, 6, 7]	# ans 4 2 1 3 6 5 7 
	root = balanced_bst_from_sorted_array(arr)
	pre_order(root)

# Time Complexity: O(n) 



