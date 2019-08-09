def add(arr):
	s = 0
	for ele in arr:
		s +=ele
	return s

l = list(map(int, input('Enter the list of number').split()))
print(add(l))
