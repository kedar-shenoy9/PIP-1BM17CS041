
n = int(input("Enter the number "))
divisors = []
for i in range(1, (n//2)+1):
	if n%i == 0:
		divisors.append(i)
divisors.append(n)
print("The list of divisors ")
for ele in divisors:
	print(ele, end = " ")
print("\n")
