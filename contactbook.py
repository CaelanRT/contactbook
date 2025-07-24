import argparse
import os
import json
from dateutil import parser as date_parser
from datetime import datetime, timedelta

#make a command line tool with flags that is a contact book that will also output birthdays coming up
#make it a script so that it can be run from anywehre in your command prompt
#add taht you need to install dateutil in your dependencies

file_path = "contactbook.json"

#creates the json file if it doesn't exist on first run
if not os.path.exists(file_path):
    with open(file_path, "xt") as f:
        f.write("[]")

class Contact:

    #constructor
    def __init__(self, name, phoneNumber, birthday):
        self.name = name
        self.phoneNumber = phoneNumber
        self.birthday = birthday

    #to string of the object
    def __str__(self):
        birthday_date = self.birthday.strftime("%Y-%m-%d") if hasattr(self.birthday, 'strftime') else str(self.birthday)
        return f"Name: {self.name} Phone Number: {self.phoneNumber} Birthday: {birthday_date}"
    
    #setting the attributes to a dictionary to serialize
    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phoneNumber,
            'birthday': self.birthday.isoformat() if hasattr(self.birthday, 'isoformat') else str(self.birthday)
        }
        
    
#add contact method
def addContact(args):
    try:
        date_obj = date_parser.parse(args.birthday)
        contact = Contact(args.name, args.phone, date_obj)
        contacts.append(contact)
        print(f'Added {contact.name} to the contact book')
    except ValueError as e:
        print(f'Error: Invalid date format "{args.birthday}". Please use a valid date format like YYYY-MM-DD.')
        return

#list contacts method
def listContact(args):
    for contact in contacts:
        print(contact)

#delete contacts method
def deleteContact(args):
    for contact in contacts:
        if contact.name == args.name:
            contacts.remove(contact)
    
    print(f'Deleted {args.name} to the contact book')

def nextBirthday(args):
    days = int(args.days)
    current_date = datetime.now()
    future_date = datetime.now() + timedelta(days=days)
    birthday_count = 0

    for contact in contacts:
        if (contact.birthday > current_date and contact.birthday < future_date):
            print(f'{contact.name} has a birthday in the next {days} days: {contact.birthday}')
            birthday_count+=1
        
    if (birthday_count == 0):
        print(f'No birthdays in the next {days} days')




#your instance variables
contacts = []

#load the data from the file a list
try:
    with open(file_path, "r") as f:
        loadedlist = json.load(f)
except json.JSONDecodeError:
    loadedlist = []

#for each item, create an object and append it to the contacts list
for item in loadedlist:
    birthday = date_parser.parse(item["birthday"]) if isinstance(item["birthday"], str) else item["birthday"]
    contact = Contact(item["name"], item["phone"], birthday)
    contacts.append(contact)

#main parser
parser = argparse.ArgumentParser(
                    prog='ContactBook',
                    description='CLI Contact Book that lists your contacts with: name, phone number and birthday. Also has functionality to tell you whose birthdays are coming up based on a specified amount of days',
                    epilog='lmfao')


#subparser
subparsers = parser.add_subparsers(dest="command")

#add functionality
add_parser = subparsers.add_parser("add", help="add a new contact to the contact book")
add_parser.add_argument('--name', required=True)
add_parser.add_argument('--phone', required=True)
add_parser.add_argument('--birthday', required=True)

#list parser
list_parser = subparsers.add_parser('list', help='list the contacts in the contact book')

#delete parser
delete_parser = subparsers.add_parser('delete', help='delete a contact')
delete_parser.add_argument('--name', required=True)

#nextbirthday parser
next_birthday_parser = subparsers.add_parser('nextbirthday', help='see the next birthdays in the list in a given time period')
next_birthday_parser.add_argument('--days', required=True)

add_parser.set_defaults(func=addContact)
list_parser.set_defaults(func=listContact)
delete_parser.set_defaults(func=deleteContact)
next_birthday_parser.set_defaults(func=nextBirthday)

args = parser.parse_args()

if hasattr(args, 'func'):
    args.func(args)

    #writing the list back to file to persist the data if there was a change
    diclist = []
    for item in contacts:
        dic = item.to_dict()
        diclist.append(dic)

    with open(file_path, "w") as f:
        json.dump(diclist, f, indent=4, sort_keys=True)