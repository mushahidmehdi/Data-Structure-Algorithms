# build a triangle whose each element is greater than previous one both on row and column.


inp  = int(input('Enter a Number of rows: '))
_num = 1
for row in range(1, inp+1):
	for col in range(1, row+1):
		print(_num, end=" ")
		_num += 1
	print()