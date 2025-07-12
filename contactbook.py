
import sys
import argparse

#make a command line tool with flags that is a contact book that will also output birthdays coming up
#have it persist and read to and from a file (json file)
#make it a script so that it can be run from anywehre in your command prompt
#make it create the files in the correct place if they don't exist and you run it the first time


class Contact:
    def __init__(self, name, phoneNumber, birthday):
        self.name = name
        self.phoneNumber = phoneNumber
        self.birthday = birthday

    def __str__(self):
        return f"Name: {self.name} Phone Number: {self.phoneNumber} Birthday: {self.birthday}"
    

def addContact(args):
    contact = Contact(args.name, args.phone, args.birthday)
    contacts.append(contact)
    print(f'Added {contact.name} to the contact book')
    
def listContact():
    for contact in contacts:
        print(contact.__str__())


#your instance variables
contacts = []

parser = argparse.ArgumentParser(
                    prog='ContactBook',
                    description='CLI Contact Book that lists your contacts with: name, phone number and birthday. Also has functionality to tell you whose birthdays are coming up based on a specified amount of days',
                    epilog='lmfao')

parser.add_argument('--name', help='name')
parser.add_argument('--phone', help='phone')
parser.add_argument('--birthday', help='birthday')

subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="add a new contact to the contact book")
add_parser.add_argument('--name', required=True)
add_parser.add_argument('--phone', required=True)
add_parser.add_argument('--birthday', required=True)

list_parser = subparsers.add_parser('list', help='list the contacts in the contact book')

add_parser.set_defaults(func=addContact)

args = parser.parse_args()

if hasattr(args, 'func'):
    args.func(args)


for contact in contacts:
        print(contact.__str__())

