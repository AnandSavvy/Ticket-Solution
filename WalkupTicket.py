from Ticket import Ticket;
class WalkupTicket(Ticket):

	def __init__(self, number = 0):
		super().__init__(number);
		if ((number >= 0) & (number < 2)):
			self.price = 50.0;
		else:
			raise ValueError();
	
	def __str__(self):
		return "Number: "+ str(self.number)+ ", Price: "+ str(self.price);