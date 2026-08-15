import json


class Contact:
    def __init__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age

    def __repr__(self):
        return f"Name: <{self.name}>, Phone: <{self.phone}>, Age: <{self.age}>"
        

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        age = int(input("Enter your age: "))
        new_contact = Contact(name, phone, age)
        self.contacts.append(new_contact)
        return self.contacts
    
    def find_contact(self):
        name = input("Input the name you are looking for: ")
        for c in self.contacts:
            if c.name == name:
                return c
        return None

    def delete_contact(self):
        name = input("Input the name you want to delete: ")
        for c in self.contacts:
            if c.name == name:
                self.contacts.remove(c)
        print("No such name found")

    def list_names(self):
        names = [c.name for c in self.contacts]
        print(names)

    def average_age(self):
        average = sum([c.age for c in self.contacts]) // len([c.age for c in self.contacts])
        print(average)

    def contacts_over(self):
        over = [c.name for c in self.contacts if c.age > 18 ]
        print(F"IT'S OVER FOR {over}")
    
    def to_dict(self):
        todict = [{"name": c.name, "phone": c.phone, "age":c.age} for c in self.contacts]
        print(todict)
        result = json.dumps(todict)
        print(result)
        
book = ContactBook()

while True:
    print("\n1. Add Contact \n2. Find Contact\n3. Delete contact\n4. List names\n5. Average age\n6. Contact over\n7. To Dictionary\nElse Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(book.add_contact())
    elif choice == "2":
        print(book.find_contact())
    elif choice == "3":
        book.delete_contact()
    elif choice == "4":
        print(book.list_names())
    elif choice == "5":
        print(book.average_age())
    elif choice == "6":
       book.contacts_over()
    elif choice == "7":
        book.to_dict()
    else:
        break

