from Date import Date

class PageInfo(object):
	date = Date(0, 0, 0)
	bidPrice = 0
	itemPrice = 0
	
	def __init__(self, date, bidPrice, itemPrice):
		self.date = date
		self.bidPrice = bidPrice
		self.itemPrice = itemPrice
	
	def __eq__(self, other):
		if type(other) != PageInfo:
			return False
		else:
			return (self.date == other.date and self.bidPrice == other.bidPrice and self.itemPrice == other.itemPrice)