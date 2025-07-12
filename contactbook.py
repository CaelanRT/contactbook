
import sys
import argparse
import os
import json

#make a command line tool with flags that is a contact book that will also output birthdays coming up
#have it persist and read to and from a file (json file)
#make it a script so that it can be run from anywehre in your command prompt

file_path = "contactbook.json"

#creates the json file if it doesn't exist on first run
if not os.path.exists(file_path):
    f = open(file_path, "xt")

class Contact:

    #constructor
    def __init__(self, name, phoneNumber, birthday):
        self.name = name
        self.phoneNumber = phoneNumber
        self.birthday = birthday

    #to string of the object
    def __str__(self):
        return f"Name: {self.name} Phone Number: {self.phoneNumber} Birthday: {self.birthday}"
    
    #setting the attributes to a dictionary to serialize
    def to_dict(self):
        "name" = self.name
        "phone" = self.phoneNumber
        "birthday" = self.birthday
    

def addContact(args):
    contact = Contact(args.name, args.phone, args.birthday)
    contacts.append(contact)
    print(f'Added {contact.name} to the contact book')
    
def listContact():
    for contact in contacts:
        print(contact.__str__())

#your instance variables
contacts = []

#load the data from the file into contacts
loadedlist = json.load()

for item in loadedlist:
    contact = Contact(item.name, item.phone, item.birthday)
    contacts.append(contact)

#main parser
parser = argparse.ArgumentParser(
                    prog='ContactBook',
                    description='CLI Contact Book that lists your contacts with: name, phone number and birthday. Also has functionality to tell you whose birthdays are coming up based on a specified amount of days',
                    epilog='lmfao')

#arguments for main parser
parser.add_argument('--name', help='name')
parser.add_argument('--phone', help='phone')
parser.add_argument('--birthday', help='birthday')

#subparser
subparsers = parser.add_subparsers(dest="command")

#add functionality
add_parser = subparsers.add_parser("add", help="add a new contact to the contact book")
add_parser.add_argument('--name', required=True)
add_parser.add_argument('--phone', required=True)
add_parser.add_argument('--birthday', required=True)

#list parser
list_parser = subparsers.add_parser('list', help='list the contacts in the contact book')

add_parser.set_defaults(func=addContact)
list_parser.set_defaults(func=listContact)

args = parser.parse_args()

if hasattr(args, 'func'):
    args.func(args)

#writing the list back to file to persist the data

