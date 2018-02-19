#coding: UTF-8
from datetime import date, datetime

print "3. Current date and time:"

# Clock in the format HH:MM:SS
print datetime.now().time()

# Today's date
#print date.now().strftime('%Y-%m-%d')

import sys

print "2. Your current version is:"

#Prints version of python running
print sys.version

# nr 7
filename = raw_input("7. Please write the name of your file: \n")

hh = filename.split('.')

print "File format is: " + hh[1]
