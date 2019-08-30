word = "brontosaurus"
count = {}
for letter in word:
	try:
		count[letter] += 1
	except KeyError:
		count[letter] = 1
print(count)
