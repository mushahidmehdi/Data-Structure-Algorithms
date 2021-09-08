
# Q-) how you could use a single array to implement three stacks (k=3) ?
# https://www.quora.com/How-can-we-implement-k-stacks-in-an-array

import pytest

class KStackSingleArray:
	def __init__(self, stack_size, stacks_numbers):
		self.stacks_numbers = stacks_numbers
		self.array = [0] * (stack_size * stacks_numbers)
		self.size = [0] * stacks_numbers
		self.stack_size = stack_size

	def check_is_valid_stack(self, stack_num):
		if stack_num >= self.stacks_numbers:
			raise OutOfRangeStackError(f'stack {stack_num} is out of range')
	
	def head(self, stack_num):
		self.check_is_valid_stack(stack_num)
		stack_over_flow = stack_num * self.stack_size
		return stack_over_flow + self.size[stack_num] - 1

	def is_empty(self, stack_num):
		self.check_is_valid_stack(stack_num)
		return self.size[stack_num] == 0

	def is_full(self, stack_num):
		self.check_is_valid_stack(stack_num)
		return self.size[stack_num] == self.stack_size

	def peek(self, stack_num):
		self.check_is_valid_stack(stack_num)
		if self.is_empty(stack_num):
			raise EmptyStackError(f'stack {stack_num} is empty, can\'t peek an empty stack')
		return self.array[self.head(stack_num)]

	def push(self, value, stack_num):
		self.check_is_valid_stack(stack_num)
		if self.is_full(stack_num):
			raise FullStackError(f'stack {stack_num} is full can\'t push more')
		self.size[stack_num] += 1
		self.array[self.head(stack_num)] = value
	
	def pop(self, stack_num):
		self.check_is_valid_stack(stack_num)
		if self.is_empty(stack_num):
			raise EmptyStackError(f'stack {stack_num} is empty, can\'t pop an empty stack')
		
		item = self.array[self.head(stack_num)]
		self.array[self.head(stack_num)] = 0
		self.size[stack_num] -= 1 
		return item

class OutOfRangeStackError(ValueError):
	"""the stack is out of range"""

class FullStackError(Exception):
	"""the stack is full"""

class EmptyStackError(Exception):
	"""the stack is empty	"""


kstack = KStackSingleArray(2, 2)
print(kstack.is_empty(0))  # True
print(kstack.is_empty(1))  # True

kstack.push(1, 0)	
kstack.push(10, 1)

print(kstack.is_empty(0))  # False
print(kstack.is_empty(1))  # False

kstack.push(2, 0)		
kstack.push(11, 1) 		
print(kstack.pop(0)) # 2
print(kstack.pop(1)) # 11

print(kstack.pop(0)) # 1
print(kstack.pop(1)) # 10




