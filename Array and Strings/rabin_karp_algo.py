# Given two patterns, find smaller pattern in the greater pattern.

# Rabin karp algorithm is pattern matching alghorithm.
# To find a sequence from a given pattern(n) usually we add up the pattern(m) which we want to find, and if the sum matches to the main pattern(n) we found the sequence index else we roll the rolling hash on next element in the sequence.

# This gives the run time of O(n - m + 1), but in the cases where there are spurious hits the sum could be the same but the pattern don't matched, in such cases the run time can goes upto O(mn).

# Here rabin karp algo came into picture. Rabin Karp algorithm used two:  
# Modular Arthmatic Hashing Function: h = (c1 X b**m-1 + c2 X b**m-2)
# Rolling Hashing Formula: b*(hash - c * b**m-1 ) + c


# https://python.plainenglish.io/a-simple-plagiarism-rate-checker-using-rabin-karp-string-matching-algorithm-in-python-e823d29d3f21

# def rabin_karp(pattern, subPattern):
# 	pattern = pattern.upper()
# 	subPattern = subPattern.upper()
# 	lenPattern = len(pattern)
# 	lenSubPattern = len(subPattern)
# 	b = 26
# 	subHash = 0
# 	hash = 0
# 	for i in range(lenSubPattern):
# 		# applying modular arthimatic formula: hash = c * b**m-i-1
# 		subHash += ((ord(subPattern[i])) * b**(lenSubPattern-i-1))
# 		hash += ((ord(pattern[i])) * b**(lenSubPattern-i-1))
# 	print(subHash)
# 	print(hash)

# 	for i in range(lenPattern-lenSubPattern+1):
# 		if i != 0:
# 			# Rolling hash formula: b*(hash - c * b**m-1 ) + c
# 			hash = b * (hash - (ord(pattern[i-1]))*(b**(lenSubPattern-1)))+ (ord(pattern[lenSubPattern+i-1]))
		
# 		if hash == subHash:
# 			return (f'Sub Pattern Index at: {i}')

# 	return False



def pattern_matching(main_pattern, sub_pattern):
	
	main_pattern = main_pattern.lower()
	sub_pattern = sub_pattern.lower()

	base = 26

	main_hash = 0
	sub_hash = 0

	for i in range(len(sub_pattern)):
		# applying modular arthimatic formula: hash = c * b**m-i-1
		sub_hash += (ord(sub_pattern[i])) * (base**(len(sub_pattern) - i - 1))
		main_hash += (ord(main_pattern[i]))* (base**(len(sub_pattern) - i - 1))

	for i in range(len(main_pattern) - len(sub_pattern) + 1):
		if i != 0:
			# Rolling hash formula: b*(hash - c * b**m-1 ) + c
			main_hash = base * (main_hash - (ord(main_pattern[i-1])) * (base**(len(sub_pattern) -1))) + (ord(main_pattern[len(sub_pattern)+i-1]))

		if main_hash == sub_hash:
			return i

def main():
    string = 'vwxy'
    seq = 'xy'
    rks = pattern_matching(string, seq)
    print(rks)

    
if __name__ == '__main__':
    main()
