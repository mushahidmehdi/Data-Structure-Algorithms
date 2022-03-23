# Given a two dimetional array retuen the highest number if it not occers twice and -1 if there is no occurance.


def cards(list:list)-> int:
	highest_number = float('-inf')
	second_highest = float('-inf')

	for i in range(len(list)):
		for j in range(len(list[i])):

			if list[i][j] == highest_number:
				highest_number = -1
			elif list[i][j] > highest_number:
				highest_number = list[i][j]

			
			
	return second_highest if second_highest < highest_number else highest_number
			
	


def main():
	cards_a = [[2,1,8,9,5,7,1,9],[1,5,2],[4,3,6,1]]
	cards_b = [[2,1,2,1]]
	print(cards(cards_a))

if __name__ =='__main__':
	main()
