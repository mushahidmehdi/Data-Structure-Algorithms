def multiplication_table(row,col):
	matrix = [[0]*col]*row
	print(matrix)
	for i in range(1,row+1):
		print('row: ' +str(i))
		for j in range(1,col+1):
			print('col: ' +str(i))
			matrix[(i-1)][(j-1)] = (i*j)
			print(matrix)
	return matrix

if __name__ == '__main__':
	print(multiplication_table(2,2))