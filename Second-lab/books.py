book_list = ['B1', 'B2', 'B3', 'B4']
price_list = [1250, 1000, 1300, 1200]
req_book = ['B3', 'B1', 'B5']
req_quantity = [3, 10, 5]
total = []

for i in range(len(req_book)):
	if req_book[i] in book_list:
		j = book_list.index(req_book[i])
		t = req_quantity[i]*price_list[j]
		total.append(req_book[i]+ " : " + str(req_quantity[i]) +" "+ str(price_list[j])+" "+ str(t))
	else:
		total.append(req_book[i]+ " : not present")

for ele in total:
	print(ele)
