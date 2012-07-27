def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses" % cheese_count
	print "you have %d boxes of crackers" % boxes_of_crackers
	print "wow\n"

print "put numbers directly to the function:"
cheese_and_crackers(20,40)

print "or use variables from scirpt: "
amount_of_cheese = 10
amount_of_crackers = 20


cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can do the math inside too"
cheese_and_crackers(2+10, 5+7)

print "and we can combine them too: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

