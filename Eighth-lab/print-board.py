def printBoard(num):
	for i in range(num):
		print(" ---" * num)
		print("|   " * (num+1))
	print(" ---" * num)

if __name__ == "__main__":
	num = int(input("Enter the number of rows and columns "))
	printBoard(num)
