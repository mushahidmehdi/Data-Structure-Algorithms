# Data Structure which is based in pile on one over the another and follow LastInFirstOur (LIFO):

class Stack:
	def __init__(self):
		self.elements = []

	def __str__(self):
		elem = [str(i) for i in self.elements]
		return ' '.join(elem)

	def push(self, data):
		self.elements.append(data)
		return data

	def pop(self):
		data = self.elements.pop()
		return data

	def peek(self):
		look = self.elements[-1]
		return look
	
	def is_empty(self):
		return len(self.elements) == 0

if __name__ == '__main__':
	stack = Stack()

	print(stack.is_empty())
	stack.push(10)
	stack.push(9)
	stack.push(8)
	stack.push(7)
	#print(stack)
	print(stack.peek())
	stack.pop()
	stack.pop()
	print(stack)