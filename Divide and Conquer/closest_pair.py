# closest pair is divide and conquer algorithem which determine the shorest length in a given number of point in 2D plane
import math
# A class to represent a Point in 2D plane
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

# distance formula to find distane b/w two points.
# https://www.gstatic.com/education/formulas2/355397047/en/distance_formula.svg

def dist(p1, p2):
	return math.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2))

