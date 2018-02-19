import os
os.system('clear')

def Contact_input():
    name = str(raw_input("Your first and last name: "))
    nr = str(raw_input("Your telephone number: "))
    email = str(raw_input("Your email adress: "))
    profile = [name, nr, email]
    return profile

def Create_contact(profile):
    document = open("Contacts.txt", "a")
    document.write("Name: " + profile[0] + "\n")
    document.write("Number: " + profile[1] + "\n")
    document.write("Email: " + profile[2]+ "\n")
    document.write("\n")

Created_profile = Contact_input()

Create_contact(Created_profile)
