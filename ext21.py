def add(a, b):
	print "adding %d + %d" % (a, b)
	return a + b

def substract (a, b):
	print "substracting %d - %d" % (a, b)
	return a - b

def multiply (a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "dividing %d / %d" % (a, b)
	return a / b

liczba1 = 10
liczba2 = 5


print "adding %d + %d = %d" % (liczba1, liczba2, add(liczba1, liczba2))
