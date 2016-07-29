def tip(bill,tip_perc):
	return bill * (tip_perc * 0.01)
# print tip(100,.18)

def total(bill, tip):
	return bill + tip
# print total(100, tip_amount)

def split_bill(bill_total, num_people):
	return bill_total / num_people

def main():
	# bill = 650
	# tip_perc = .12
	# people = 2
	# tip_amount = tip(bill, tip_perc)
	# bill_total = total(bill, tip_amount)
	# # bill_split = split_bill(bill_total,people)
	# return bill_split

	calculated_bill = float(raw_input("How much was your bill?"))
	desired_tip = float(raw_input ("How much do you want to tip?"))
	choice = raw_input("What would you like to do? 1 - Calculate tip 2- Split the bill")
	tip_total = tip(calculated_bill, desired_tip)
	total_amount = tip_total + calculated_bill

	if choice == "1":
		print tip_total
		print total_amount
	elif choice == "2":
		people = float(raw_input("How many people are in your party?"))
		per_person = split_bill(total_amount, people)
		print "The cost per person is:", per_person, "for", people, "persons."

if __name__ == '__main__':
   main()