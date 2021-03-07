# 建立記帳程式

products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break # 若輸入q則代表結束，跳出迴圈
	price = input('請輸入商品價格: ') # 若沒有輸入商品名稱，則不用再輸入price，因此放在break之下

	# 製作二維清單來儲存商品與價格：[[商品1, 價格1], [商品2, 價格2], [商品3, 價格3],...]
	p = [name, price]
	products.append(p)

print('\n')
# 印出每一項對應的價格
for items in products:
	print(items[0], '的價格是', items[1])