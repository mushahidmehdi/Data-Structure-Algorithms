# given a numbers of candies: distribute it among children based on following constrains:
# Each child get one candy. 
# Children with higher number of rating get more candy 1 more candy to their neighbors candy.
# To solve this problem we will traverse through chidren rating by comparing rating of each child from to its left neighbors then again travering the rating from right neighbors by revering the list and chossing max out of two:

def distruting_candy(rating):
	# each child get 1 candy
	LtoR = [1 for i in range(len(rating))]
	RtoL = [1 for i in range(len(rating))]
	candyDistributed = []
	# first by comparing from its left neighbor:
	for i in range(1,len(rating)):
		if rating[i-1] < rating[i]:
			LtoR[i] += LtoR[i-1]
	
	for i in range(1,len(rating)):
		if rating[::-1][i-1] < rating[::-1][i]:
			RtoL[i] += RtoL[::-1][i-1]
	
	for i in range(len(rating)):
		candyDistributed.append(max(LtoR[i], RtoL[i]))
	
	return candyDistributed

def main():
	rating =[2,4,1,7,9]
	print(distruting_candy(rating))
		
if __name__ == '__main__':
	main()
			

