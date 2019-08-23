def search(arr, n):
	return n in arr

l = list(map(int, input("Enter the list ").split()))
n = int(input("Enter the number "))
print(search(l, n))
