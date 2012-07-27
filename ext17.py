from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "kopiujemy plik %s do pliku %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "zawartosc pliku jest %d bytes dluga" % len(indata)

print "istnieje plik docelowy ? %r" % exists(to_file)
print "dalej: enter, przerwac: CTRL+C"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "done"

out_file.close()
in_file.close()
