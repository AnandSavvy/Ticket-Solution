
# DO NOT Change this code, it will be used as base for all testings...
class Ticket:
	number = 0;		# Ticket Number is defined by constructor
	price = 0.0;	# Price determined by sub-class

	numSold = 0;			# total tickets sold
	maxSales = 1000;		# max sales allowed

	sold = [False] * maxSales;		# tells us if that index (number) is sold.
	#print (len(sold));		size: 1000
	#[True, True, False, ... 10000]
	# Constructor
	def __init__(self, value):
		Ticket.numSold = Ticket.numSold +  1;
		while (Ticket.sold[value]):
			value = value + 1;			# find next available unique ticket number
		Ticket.sold[value] = True;
		self.number = value;			# Ticket constructor sets number

	# ACCESSORS
	def getPrice(self):
		return self.price;			# set by sub-class constructors

	# Python standard str method...
	def __str__(self):
		return "Number: "+ str(self.number) + ", Price: " + str(self.getPrice());


# [True, True, True, False.....1000]