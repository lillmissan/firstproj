name = input("What's your name?")
birthplace = input("Where were you born?")
favcolor = input ("What's your favourite color?")

file = open("ree.txt")
file.write("\n" + name, + " " + birthplace, + " " + favcolor)
file.close()
