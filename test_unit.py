#n = 4
##for i in range(n - 1, -1, -1):
##	print(i)
#new_matrix = [[0]*3 for i in range(n)]
#print(new_matrix)


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix

print(zero_matrix([[1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25]]))