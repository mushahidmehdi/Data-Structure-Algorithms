# Given two patterns, find smaller pattern in the greater pattern.
# Rabin karp algorithm is pattern matching alghorithm.
# To find a sequence from a given pattern(n) usually we add up the pattern(m) which we want to find, and if the sum matches to the main pattern(n) we found the sequence index else we roll the rolling hash on next element in the sequence.
# This gives the run time of O(n - m + 1), but in the cases where there are spurious hits the sum could be the same but the pattern don't matched, in such cases the run time can goes upto O(mn).

# Here rabin karp algo came into picture. Rabin Karp algorithm used two:  
# Modular Arthmatic Hashing Function: h = (c1 X b**m-1 + c2 X b**m-2)
# Rolling Hashing Formula: b*(hash - c * b**m-1 ) + c


def rabin_karp(pattern, subPattern):
	pattern = pattern.upper()
	subPattern = subPattern.upper()
	lenPattern = len(pattern)
	lenSubPattern = len(subPattern)
	b = 26
	subHash = 0
	hash = 0
	for i in range(lenSubPattern):
		# applying modular arthimatic formula: hash = c * b**m-i-1
		subHash += ((ord(subPattern[i])) * b**(lenSubPattern-i-1))
		hash += ((ord(pattern[i])) * b**(lenSubPattern-i-1))
	print(subHash)
	print(hash)

	for i in range(lenPattern-lenSubPattern+1):
		if i != 0:
			# Rolling hash formula: b*(hash - c * b**m-1 ) + c
			hash = b * (hash - (ord(pattern[i-1]))*(b**(lenSubPattern-1)))+ (ord(pattern[lenSubPattern+i-1]))
		
		if hash == subHash:
			return (f'Sub Pattern Index at: {i}')

	return False

def main():
    string = 'vwxy'
    seq = 'xy'
    rks = rabin_karp(string, seq)
    print(rks)

    
if __name__ == '__main__':
    main()
# https://python.plainenglish.io/a-simple-plagiarism-rate-checker-using-rabin-karp-string-matching-algorithm-in-python-e823d29d3f21