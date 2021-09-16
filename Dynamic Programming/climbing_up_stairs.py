#  A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

# We can implement this problem recursively:
# if the child move 1 step, remaing would be n-1
# similary, if child hop 2, or 3 steps; remaining steps would be n-2 or n-3 respectively.
# keep running recursively, until we reach the base case where either there are no more stairs, 1 or 2 stairs.
def running_up(stairNum):
	if stairNum == 0 or stairNum == 1:
		return 1
	elif stairNum == 2:
		return 2
	else:
		return running_up(stairNum-3) + running_up(stairNum -2) + running_up(stairNum-1)


# this problem can be solved using dynamic programming:
def top_stair(stairNum):
	# initially to all the stairs would be 0 as there is no hopping up
	steps = [0]*(stairNum+1)
	# To reach the 1st stairs it would take 1 step only, similary to reach 2nd step it would take 2 1 steps or 1 2 steps which mean there would be 2 ways.
	steps[0] = 1
	steps[1] = 1
	steps[2] = 2
	for i in range(3, stairNum+1):
		steps[i] = steps[i-1] + steps[i-2] + steps[i-3]
	return steps[stairNum]





def main():
	stairNum = 10
	#stairNum = 4
	print(running_up(stairNum))
	print(top_stair(stairNum))

if __name__ == '__main__':
	main()