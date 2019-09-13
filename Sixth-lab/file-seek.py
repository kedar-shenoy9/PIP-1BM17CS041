#f = open("file_1.txt", "r")
#contents = f.read()
#print(contents[::-1])
#f.close()

output = ""
with open("file_1.txt", "r") as f:
	i = 0
	fileLength = len(f.read())
	while i<fileLength-1:
		f.seek(fileLength-2-i,0)
		output += f.read(1)
		i += 1

print(output)
