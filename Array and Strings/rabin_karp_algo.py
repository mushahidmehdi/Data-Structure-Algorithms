# Rabin karp algorithm is pattern matching alghorithm......!
# To find a sequence from a given pattern(n) usually we add up the pattern(m) which we want to find, by assaining numerical value to each, and the sum of the number matching to the actual within  pattern(n) such in the way that the sum of searching(m) sequence and the hidden sequence in (m) will have same sum if the sum match then we compare the sequence else we roll the rolling hash. this gives the run time of O(n - m + 1), but in the cases where there are spurious hits the sum could be the same but the pattern don't matched, in such cases the run time can go O(mn). Here rabin karp algo came into picture; by giving each index their coresponding base positition and and rasing the hash map to the power.


def rabin_karp(string,pat):
    string = string.upper()
    pat = pat.upper()
    #ASSUMING ALL CHARACTERS ARE UPPPER_CASE,
    #Can be extended for lower case if necessary
    
    l = len(string)
    l_p = len(pat)
    con = 26 #The constant for base system 26
    
    hashval = 0    #For the pattern
    currhash = 0 #For each substring
    for i in range(l_p):
        # Modular arithmetic hash function:
        # hash value as coefficient - c; len of sequence as base (b), len of sequence. h = (c1 X b**m-1 + c2 X b**m-2)
        hashval += (ord(pat[i])-ord('A')+1)*(con**(l_p-i-1))
        currhash += (ord(string[i])-ord('A')+1)*(con**(l_p-i-1))    
    for ind in range(l-l_p+1):
        if ind!=0:
            # Rolling Hash formula:
            # Hash = b*(h - c*b**m-1) + c
            currhash = con*(currhash-((ord(string[ind-1])-ord('A')+1)*(con**(l_p-1))))+(ord(string[ind+l_p-1])-ord('A')+1)
  
        if(currhash==hashval):
            print("Found at index",ind)
            return True
    return False

def main():
    string = 'vwxy'
    seq = 'xy'
    rks = rabin_karp(string, seq)
    print(rks)

    
if __name__ == '__main__':
    main()
	

# https://python.plainenglish.io/a-simple-plagiarism-rate-checker-using-rabin-karp-string-matching-algorithm-in-python-e823d29d3f21