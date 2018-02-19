restrict = ["cigarettes", "tobacco", "redbull", "alcohol"]

order = str(raw_input("What do you want to buy?" + "\n"))

if order in restrict :
    print "Legitimation please."
elif order not in restrict :
    print "That will be $ blabla.50"
else :
    print "faaaaaaaak"
