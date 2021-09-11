# Basics of programmming

def hanoi(n, src, helper, target):
	if n > 0:
		# move n-1 from src to helper
		hanoi(n-1, src, target, helper)
		if src:
			target.append(src.pop())
		# move tower of size n-1 from helper to target
		hanoi(n-1, helper, src, target)

def main():
	source = [6,5,4,3,2,1]
	target = []
	helper = []
	hanoi(len(source), source, helper, target)
	print(source)
	print(helper)
	print(target)

if __name__ == '__main__':
	main()

# https://runestone.academy/runestone/books/published/pythonds/Recursion/TowerofHanoi.html


