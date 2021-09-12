# given a statement find wether all the parenthesis are balanced or not.

# To solve this problem we will used a stack data structure; Last in First out, if the parenthesis are at their opening part then we will apend he parenthesis into the stack else if the parenthsis is at their closeing part we will check whether if it match with the last append opening parenthesis or if the stack is empty, if any of these condition are True the statement doen't have balanced parenthesis. 

from collections import deque
import unittest



def check_bal_paren(paren, pair):
	stack = deque()
	for i in range(len(paren)):
		if paren[i] in pair:
			stack.append(paren[i])
		else:
			if len(stack) == 0 or pair[stack[-1]] != paren[i]:
				return False
			else:
				stack.pop()
	return len(stack) == 0

class Test(unittest.TestCase):

	def test_balanced_parenthesis(self):
		pair = {'(':')','{':'}','[':']'}
		a = '[]'
		b = '{{{{}}}}()()()(())[[[[]]]]'
		c = '))((())[[][[]]'
		d = '[(])'
		e = ('{{([][])}()}')  
		f = ('{[])')  
		g =('((()))')  
		h =('(()')  
		i =('())')  
		
		self.assertTrue(check_bal_paren(a, pair))
		self.assertTrue(check_bal_paren(e, pair))
		self.assertTrue(check_bal_paren(g, pair))
		self.assertTrue(check_bal_paren(b, pair))
		self.assertFalse(check_bal_paren(c, pair))
		self.assertFalse(check_bal_paren(d, pair))
		self.assertFalse(check_bal_paren(f, pair))
		self.assertFalse(check_bal_paren(h, pair))
		self.assertFalse(check_bal_paren(i, pair))


if __name__ == '__main__':
	unittest.main()
	
