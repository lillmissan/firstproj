def compare(a,b):
    if a > b :
        print "%i is bigger than %i!"%(a,b)
    elif b > a :
        print "%i is bigger than %i!"%(b,a)
    elif a == b :
        print "%i and %i are equal."%(a,b)
    else :
        print "Oops, something went wrong. Are you sure you used numbers?"

compare(5,6)
