# https://medium.com/@emmabostian/creating-3-stacks-with-1-array-in-javascript-e1171d661e89

# Q-) how you could use a single array to implement three stacks (k=3) ?

class KStackSingleArray:
	def __init__(self, _stack_size, stack_numbers):

		# he maximum number of elements that can fit into one stack. in other word length of the stack.
		self._stack_size = _stack_size

		# number of stacks allowed in an array to hold. 
		self.stack_numbers = stack_numbers

		# An array which contains of all elements in the three stacks
		self.array = [0] * (_stack_size * stack_numbers)

		# number of elements in each array in their respective stacks.
		self.size = [0] * stack_numbers

	def check_is_valid_stack(self, stack_num):
		# the index of self.stack_number begins with 0
		if stack_num >= self.stack_numbers:
			raise OutOfRangeStackError(f'stack {stack_num} is out of range')
	
	def indexOfTop(self, stack_num):
		self.check_is_valid_stack(stack_num)
		stack_over_flow = stack_num * self._stack_size
		# stack index begins with 1 but array begins with 0;
		return stack_over_flow + self.size[stack_num] - 1

	def is_empty(self, stack_num):
		self.check_is_valid_stack(stack_num)
		return self.size[stack_num] == 0

	def is_full(self, stack_num):
		self.check_is_valid_stack(stack_num)
		# if number of elements in a stack == stack_size(lenght)
		return self.size[stack_num] == self._stack_size

	def peek(self, stack_num):
		self.check_is_valid_stack(stack_num)
		if self.is_empty(stack_num):
			raise EmptyStackError(f'stack {stack_num} is empty, can\'t peek an empty stack')
		return self.array[self.indexOfTop(stack_num)]

	def push(self, value, stack_num):
		self.check_is_valid_stack(stack_num)
		if self.is_full(stack_num):
			raise FullStackError(f'stack {stack_num} is full can\'t push more')
		self.size[stack_num] += 1
		self.array[self.indexOfTop(stack_num)] = value
	
	def pop(self, stack_num):
		self.check_is_valid_stack(stack_num)
		if self.is_empty(stack_num):
			raise EmptyStackError(f'stack {stack_num} is empty, can\'t pop an empty stack')
		
		item = self.array[self.indexOfTop(stack_num)]
		self.array[self.indexOfTop(stack_num)] = 0
		self.size[stack_num] -= 1 
		return item

class OutOfRangeStackError(ValueError):
	"""the stack is out of range"""

class FullStackError(Exception):
	"""the stack is full"""

class EmptyStackError(Exception):
	"""the stack is empty	"""


kstack = KStackSingleArray(4, 4)
print(kstack.is_empty(0))  # True
print(kstack.is_empty(1))  # True
print(kstack.is_empty(2))  # True
print(kstack.is_empty(3))  # True


kstack.push(1, 0)	
kstack.push(2, 0)
kstack.push(3, 0)

# print(kstack.is_empty(0))  # False
# print(kstack.is_empty(1))  # False
# print(kstack.pop(0)) # 3
# print(kstack.pop(0)) # 2

# print(kstack.pop(0)) # 1
# print(kstack.pop(1)) # 10

print(kstack.indexOfTop(0))


