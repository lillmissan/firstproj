import os
os.system('clear')

file = open("hello.txt").read()
n = 0

while n == 0:
    word = raw_input("Search for word: ")

    if word in file:
        print "The word %r is in the text." %(word)
        n = 1
    else:
        print "The word %r is not in the text." %(word)
