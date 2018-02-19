file = open("hello.txt")

def newLine(text):
    counter = 1
    for line in text:
        print "%i : %s"%(counter,line)
        counter += 1

newLine(file)
