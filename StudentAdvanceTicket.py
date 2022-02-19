from AdvanceTicket import AdvanceTicket

class StudentAdvanceTicket(AdvanceTicket):
	def __init__(self, number = 0, days = 0):
		super().__init__(number, days);

		if (self.getDays() < 0):
			raise ValueError();
		elif (self.getDays() >= 10):
			self.price = 15.0;
		else:
			if (self.getDays() == 0):
				self.price = 50.0;
			else:
				self.price = 20.0;

	def __str__(self):
		if (self.price <= 20.0):
			return super().__str__() + " (ID required)";
		else:
			return super().__str__();