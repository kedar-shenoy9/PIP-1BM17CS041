arr = list(map(int, input("Enter the list of numbers ").split()))
evenList = []
for ele in arr:
	if ele%2 == 0:
		evenList.append(ele)
print("The list of even numbers in the given list is ")
print(evenList)
