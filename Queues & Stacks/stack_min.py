# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

# in this vedio expalins the nuance in very subtle way:
# https://www.youtube.com/watch?v=ufwPuyxkNVE
# in the nut shell, push in main_stack always but in auxi_stack only if < than top value same for pop if both value are == pop from both else only from main.



from collections import deque

class MinimumStack:
	def __init__(self):
		self.main_stack = deque()
		self.auxi_stack = deque()

	def push(self, item):
		self.main_stack.append(item)
		
		if not self.auxi_stack:
				self.auxi_stack.append(item)
		else:
			if item <= self.auxi_stack[-1]:
				self.auxi_stack.append(item)

	def pop(self):
		if self.is_empty():
			return ('stack is empty')
		top = self.main_stack.pop()
		if top == self.auxi_stack[-1]:
			self.auxi_stack.pop()
		return top

	def is_empty(self):
		return len(self.main_stack) == 0

	def min(self):
		if not self.auxi_stack:
			return ('stack underlow')
		return self.auxi_stack[-1]


if __name__ == '__main__':
	stack = MinimumStack()
	#print(stack.is_empty())
	#stack.push(6)
	#print(stack.is_empty())
	#stack.push(7)
	#stack.push(8)
	#stack.push(4)
	#stack.push(9)s
	print(stack.pop())
	print(stack.min())

	
