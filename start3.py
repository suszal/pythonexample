class Product(object):
	def price_with_vat(self):
		return self.price*self.count*self.vat
	price=0
	count=0
	vat=1

robot=Product()
robot.price=900
robot.count=2
robot.vat=1.25

book=Product()
book.price=100
book.count=1
book.vat=1.06


print robot.price_with_vat() + book.price_with_vat()