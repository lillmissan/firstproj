print "Hello! What is your name?"
name = raw_input(prompt)

print "How old are you?"
age = raw_input(prompt)

hundred = 2017 + (100 - int(age))

print "Oh, %r ! The year of %s you turn 100 years old!"%(name, hundred)
