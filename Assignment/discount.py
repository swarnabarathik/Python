original_price=int(input("enter the amount"))
if(original_price>500):
	discount_price=original_price-(original_price*2/100)
	print("Discounted amount:%d"%discount_price)
else:
	discount_price=original_price-(original_price*1/100)
	print("Discounted amount:%d"%discount_price)
	
