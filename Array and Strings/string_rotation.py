
# Rotate the string based on the given integer values for leftshift and rightshift, all test cases passed.
# Input: s = "abcde", goal = "cdeab"
# Output: true
# Input: s = "abcde", goal = "abced"
# Output: false

def rotate_string(inp: str, out: str) -> bool:
	return len(inp) == len(out) and out in inp + inp



def main():
	inp = "abcde"
	out = "cdeab"
	inp2 = "abcde"
	out2 = "abced"
	ans = rotate_string(inp2, out2)
	print(ans)
if __name__ == '__main__':
	main()