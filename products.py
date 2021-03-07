# 讀取已儲存的檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue # continue的意思是，跳過這一圈，可以藉此方式來避免儲存到'商品,價格'這一行
		name, price = line.strip().split(',') # strip()去除換行符號		# split(',')代表依據逗號分割，分割後的資料會形成list   

		products.append([name,price])         
print(products)

# 建立記帳程式：讓使用者輸入商品與價格
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break # 若輸入q則代表結束，跳出迴圈
	price = input('請輸入商品價格: ') # 若沒有輸入商品名稱，則不用再輸入price，因此放在break之下

	# 製作二維清單來儲存商品與價格：[[商品1, 價格1], [商品2, 價格2], [商品3, 價格3],...]
	p = [name, price]
	products.append(p)

print('\n')

# 印出所有購買紀錄
for items in products:
	print(items[0], '的價格是', items[1])


# 將所有購買紀錄寫入檔案
with open('products.csv', 'w') as f: # 讀取與寫入檔案的起手式
	f.write('商品,價格\n') # 加入header
	for i in products:
		f.write(i[0] + ',' + i[1] + '\n') # 字串可以相加
		                                  # write:寫入功能 
										  # 在CSV檔中，逗號相當於跳到右邊的欄位
										  # '\n'讓下一個item的資料換行

