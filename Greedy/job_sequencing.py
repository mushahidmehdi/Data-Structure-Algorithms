# Given a sets of tasks with deadlines and total profit, design a schedule a list in a manner that maximize the profit.
# Remeber each task will take only unit time.

# https://www.techiedelight.com/job-sequencing-problem-deadlines/

# As we can see that this problem suggests to generate maxi profit for given time, therefore this is optimization problem other word greedy algorithm.

# To Solve: We will arrage all the profit in decending order and check for the deathline slot and assign the higest profit job before its deadline.


# Job has three attibute: id, deadline and profit.
class Job:
	def __init__(self, taskId, deadline, profit):
		self.taskId = taskId
		self.deadline = deadline
		self.profit = profit
	

def schedule_job(jobs, total_hour):
	profit = 0
	# initializing each unit hour slot with -1
	time_slot = [-1]*total_hour
	# sort all the jobs based on their profit amount.
	jobs.sort(key=lambda x : x.profit, reverse=True)
	for job in jobs:
		for d in reversed(range(job.deadline)):
			if d < total_hour and time_slot[d] == -1:
				time_slot[d] = job.taskId
				profit += job.profit
				break
	print(f'The selected Jobs are:', list(filter(lambda x: x != -1, time_slot)))
	return (f'Total profit from above Jobs is: {profit}')

def main():
	jobs = [(1,9,15),(2,2,2),(3,5,18),(4,7,1),(5,4,25),(6,2,20),(7,5,8),(8,7,10),(9,4,12),(10,3,5)]
	Jobs = list()
	for job in jobs:
		id, time, profit = job
		Jobs.append(Job(id, time, profit))
	js = schedule_job(Jobs, 15)
	print(js)
	

if __name__ == '__main__':
	main()
