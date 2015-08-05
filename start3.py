class Product(object):
	price=0
	count=0
	vat=1

robot=Product()
robot.price=900
robot.count=2
robot.vat=1.25

book=Product()
book.price=100
book.vat=1.06


print robot.price*robot.count*robot.vat+book.price*book.vat