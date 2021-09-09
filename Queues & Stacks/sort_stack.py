# Write a program to sort a stack such that the smallest items are on the top. You can use  an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and is Empty. 
# To sort a stack-1 in acending order we will used stack-2 which would be contain the sorted elements of stack-1
# simply, check for last item of stack-2 if it is greater than incomming element than remove and append into stack-1 and keep comparing in this manner until, there is no more element in the stack-2 which is greater than incoming element.
from collections import deque

class StackSorting:
	def __init__(self):
		self.stack = deque()
		self.auxi = deque()

	def push(self, data):
		self.stack.append(data)
	
	def pop(self):
		if self.is_empty(self.stack):
			raise ValueError('The list is Empty..')
		return self.stack.pop()
	
	def peek(self):
		if self.is_empty(self.stack):
			raise ValueError('The list is Empty..')
		return self.stack[-1]

	def is_empty(self, stack):
		return len(stack) == 0
	
	def sort(self):
		while self.is_empty(self.stack) != True:
			temp = self.stack.pop()
			while self.is_empty(self.auxi) != True and self.auxi[-1] > temp:
				self.stack.append(self.auxi.pop())
			self.auxi.append(temp)
		return self.auxi

	def __str__(self) -> str:
		return str(self.stack)

if __name__ == '__main__':
	sort = StackSorting()
	keys = [89, 71, 45, 31, 99, 918, 46, 55]
	for i in keys:
		sort.push(i)
	print(sort)
	print(sort.peek())
	print(sort.pop())
	print(sort.sort())