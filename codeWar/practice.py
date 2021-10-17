
if __name__ == '__main__':
	pass 

print([i for i in filter(lambda x : x % 5, islice(count(5)))])