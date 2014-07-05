class Date(object):
	year = '0'
	month = '0'
	day = '0'
	
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
	
	def display(self):
		return self.year + '-' + self.month + '-' + self.day
	
	# called when Date is printed
	def __str__(self):
		return self.display()
	
	def __repr__(self):
		return self.display()
	
	def __eq__(self, other):
		if type(other) != Date:
			return self.display() == other
		elif self.display() == other.display():
			return True
		else:
			return False
	
	def __cmp__ (self, other):
		if self.year > other.year:
			return 1
		elif self.year < other.year:
			return -1
		else:
			if self.month > other.month:
				return 1
			elif self.month < other.month:
				return -1
			else:
				if self.day > other.day:
					return 1
				elif self.day < other.day:
					return -1
				else:
					return 0
			