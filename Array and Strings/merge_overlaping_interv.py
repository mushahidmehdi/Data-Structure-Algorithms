# merge overlaping interval: Explanation.
# https://www.educative.io/m/merge-overlapping-intervals

from collections import deque
class Pair:
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end

	def __str__(self):
		return str((self.begin, self.end))


def merge_overlap_interval(pair):
	stack = deque()
	# sorting by begenning time.
	pair = sorted(pair, key=lambda x : x.begin, reverse=False)
	for curr in pair:
		if not stack or curr.begin > stack[-1].end:
			stack.append(curr)

		if stack[-1].end < curr.end:
			stack[-1].end = curr.end
		
	while stack:
		print(stack.pop())
	
def main():
	timePairs = [(1,4),(3,6),(9,15),(22,40),(40,44),(49,50),(50,60)]
	pair = []
	for i in timePairs:
		start, end = i
		pair.append(Pair(start, end))
	merge_overlap_interval(pair)

if __name__ == '__main__':
	main()