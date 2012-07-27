from sys import argv

script, user_name = argv
prompt = '> '

print "what user: %s , what script: %s" % (user_name, script)

print "what day %s ?" % user_name

day = raw_input(prompt)


month = raw_input(prompt)


print """
so the day %s %s a user %s run %s
""" % (day, month, user_name, script)

