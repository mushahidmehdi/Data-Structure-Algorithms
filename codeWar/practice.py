
# Draw an IsoSelsus triangle.


triangle = 10
for i in range(triangle):
	print(" "*(triangle-i+1) + "*"*(i*2+1))







# Find whether an input sequence is Plandromic or not?

i = input("Enter a object: ")
b = i[::-1]
if b == i:
	print(i, "contains Plandromic sequence")
else:
	print(i, "No sequence detected")





# Write a program to execute bubble sort alogorithem

list = [1, 3, 5, 33, 6, 7, 8, 9, 12, 18]
def bub_sort(arr):
	n = len(arr) - 1
	for i in range(n):
		for j in range(n-i):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	print(arr)

bub_sort(list)




# Write fibonacci for a list of objects
def recur_fibo(n):
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n - 2))

ntimes = 10

if ntimes <= 0:
	print("Please Enter a Positive Number")

else:
	print('Fibonaci Sequence: ')
	list = []
	for i in range(ntimes):
		list.append(recur_fibo)
	print(list)



# Find wether the input is prime or not?

num = int(input('Please Enter a Number: '))
if num > 1:
	for i in range(2, num):
		if (num%i) == 0:
			print(num, 'is not a prime')
			print(num,'is divisible by',num//i)
			break
		else:
			print(num,'num is a prime')
else:	print(num, 'is not a prime')



# Write a sorting algorithm for a numerical dataset
a = ['19', '52', '3', '49', '6', '10', '16']
arr = []

for i in a:
	arr.append(int(i))
	arr.sort()
#print(arr)


# Write a one-liner that will count the number of capital letters in a file.
with open('forest-cover-dataset.csv') as tf:
	count = 0
	text = tf.read()
	for i in text:
		if i.isupper():
			count += 1

#print("number of capital in text",count)

# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverse(a):
	string = str(a)

	if string[0] == '-':
		return int('-' + string[:0:-1])
	else:
		return string[::-1]

#print(reverse(456789))
#print(reverse(-12345))
#print(reverse(987654321))

# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.


sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def avg_word_lenght(s):

	# First Of all Remove all the punctions
	for p in ",.!":
		pfs = s.replace(p, '')

	words = pfs.split()
	return round(sum(len(word) for word in words)/len(words), 2)

#print(avg_word_lenght(sentence1))
#print(avg_word_lenght(sentence2))

#___________________________________________________________________________
#


# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.



def two_sum(a,b):
	#a = int(a)
	#b = int(b)
	return eval(a) + eval(b)

	return a + b

num1 = '111'
num2 = '222'

# print(two_sum(num1, num2))


# Find the first occurance of string
def first_occu(a):
	frequency = {}
	for i in a:
		if i not in frequency:
			frequency[i] = 1
		else:
			frequency[i] += 1
		
	for n in range(len(a)):
		if frequency[a[n]] == 1:
			return n
	return -1

#print(first_occu('alphabet'))
#print(first_occu('barbados'))
#print(first_occu('crunchy'))



# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def palin(a):
	for i in range(len(a)):
		l = a[:i] + a[i+1:]
		if l == l[::-1]:
			return True
	return a == a[::-1]

#print(palin('abujijijijocba'))
