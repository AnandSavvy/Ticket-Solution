from Ticket import Ticket
from WalkupTicket import WalkupTicket
from AdvanceTicket import AdvanceTicket
from StudentAdvanceTicket import StudentAdvanceTicket;

class TicketTester(WalkupTicket,StudentAdvanceTicket):
	
	for tick in range(0,15):		
		tick = WalkupTicket();		# Actually calls constructor for each time.
		# First 15 tickets were reserved. So they do not exist or not available to book those ticket numbers;

	print (AdvanceTicket(10,20));	# Here is ticket number 10, purchased 20 days in advance; So, Ticket Number: 15, Price: 30.0
	print (AdvanceTicket());		# Must print ticket unique number and relevent price. Number: 16, Price: 50.0

	print (WalkupTicket(1));	# 2 attempted, but not allowed. if 1, Number: 17, Price: 50.0
	print (WalkupTicket());		# Must print ticket unique number (sequencially) and price for walkup Ticket.

	print (StudentAdvanceTicket(99,9));	# Number: 99, price: 20.0 and must print as "(ID required)" as he/she is a student.
	print (StudentAdvanceTicket());		# Number: (Auto generated unique & sequencial number), Price: 50.0. Do not required to print as (ID required)

	print (AdvanceTicket(99,10));	# 99 already used? So With above, Number: 100, Price: 40.0
	print (StudentAdvanceTicket(99, 20));

	print (WalkupTicket())
	print (StudentAdvanceTicket(30, 30))
	print (StudentAdvanceTicket(10, 20))

	print (AdvanceTicket(30, 40))

	print (StudentAdvanceTicket(899, 20 ))

	print (AdvanceTicket(899, 16))

	print (WalkupTicket())