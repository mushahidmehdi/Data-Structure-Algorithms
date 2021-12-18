# merge overlaping interval: Explanation.
# https://www.educative.io/m/merge-overlapping-intervals

# sort all the intervals with beggining value.
from collections import deque

class Class:
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end


def merging_intervals(arr):
	# sort all the pairs with beggining time intervals:
	# sorted it doesn't change the original arr
	sort_pairs = sorted(arr, key=lambda x: x.begin, reverse=False)
	stack  = deque()
	for pair in sort_pairs:
		if not stack or stack[-1].end < pair.begin:
			stack.append(pair)

		if stack[-1].end < pair.end:
			stack[-1].end = pair.end

	while stack:
		i = stack.pop()
		print((i.begin, i.end))


def main():
	timePairs = [(1,4),(3,6),(9,15),(22,40),(40,44),(49,50),(50,60)]
	pairs_objs = []
	for pair in timePairs:
		begin, end = pair
		pairs = Class(begin, end)
		pairs_objs.append(pairs)
	merging_intervals(pairs_objs)


if __name__ == '__main__':
	main()





