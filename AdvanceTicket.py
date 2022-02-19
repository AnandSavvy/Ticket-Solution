from Ticket import Ticket

class AdvanceTicket(Ticket):
	days = 0;

	def __init__(self, number = 0, days = 0):
		super().__init__(number);
		self.days = days;

		if (days < 0):
			raise ValueError();
		elif(days >= 10):
			self.price = 30.0;
		else:
			self.price = 40.0;
	
	def getDays(self):
		return self.days;

	def __str__(self):
		return "Number: "+ str(self.number)+ ", Price: "+ str(self.price);

