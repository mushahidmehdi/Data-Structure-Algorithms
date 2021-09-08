# Write a program to sort a stack such that the smallest items are on the top. You can use  an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and is Empty. 



class StackSorting:
	def __init__(self, inputs):
		self.input_stack = inputs
		self.auxi_stack = []

	def is_empty(self, stack):
		return len(stack) == 0

	def push(self, item):
		self.input_stack.append(item)

	def pop(self):
		return self.input_stack.pop()

	def peek(self, stack):
		if not self.is_empty(stack):
			return stack[-1]
		return("Empty Stack")
		

	def sort(self):
		while self.is_empty(self.input_stack) != True:
			temp = self.input_stack.pop()
			while self.is_empty(self.auxi_stack) != True and self.auxi_stack[-1] > temp:
				item = self.auxi_stack.pop()
				self.input_stack.append(item)
			self.auxi_stack.append(temp)
		return self.auxi_stack
			



if __name__ == '__main__':
	stack = StackSorting([200,12,2,34,6,8,23,4,1,10, 100])
	stack.push(7)
	print(stack.pop())
	print(stack.sort())