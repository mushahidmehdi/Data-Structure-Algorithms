#  Strassen algorithm is faster than the standard matrix multiplication algorithm for large matrices.
# https://en.wikipedia.org/wiki/Strassen_algorithm
import numpy as np

def pythonic_mtx_multi(arr1, arr2):
	return arr1.dot(arr2)

def main():
	a = np.array([[ 5, 1 ,3], 
            [ 1, 1 ,1], 
            [ 1, 2 ,1]])
	b = np.array([1, 2, 3])
	mtx = pythonic_mtx_multi(a, b)
	print(mtx)

if __name__ == '__main__':
	main()