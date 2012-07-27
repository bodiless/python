from sys import argv

script, filename = argv

print "czyscimy plik %r: " % filename
print "zeby przerwac nacisnij CTRL+C"
print "zeby przejsc dlaje nacisnij ENTER"

raw_input("?")

print "otwieram plik..."
target = open(filename, 'w')

print "czyszcze plik...Bye"
target.truncate()

print "napisz jakis tekst"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "teraz wpisuje linie do pliku..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("zamykam plik...")
target.close()
