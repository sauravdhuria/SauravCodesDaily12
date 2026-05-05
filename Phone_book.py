class PhoneBook:
    phone_contact=[] #store contact information #class variable
                    # (shared to instance&class methods)
    def __init__(self,name,phone_Number):
        self.name=name
        self.phone_Number=phone_Number

        PhoneBook.phone_contact.append(self)

    #instance method for showing contacts
    """
    
    instance because it is bound to object 
    
    """

    def show_contact(self):

        for contact in self.phone_contact:
            print(f"Contact name {self.name} Phone Number {self.phone_Number}")
        return F"Name: {self.name} ,Phone Number: {self.phone_Number}"  # Only 1 contact is
            # displayed which is bound to object

    """
    To get all the contact at one go we need to use class method
    """

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_contact)==0:
            print("No contact found in the phone book")
        else :
            for contact in cls.phone_contact:
                print(f"Contact name {contact.name} Phone Number {contact.phone_Number}")

s1=PhoneBook("Saurav",7208467235)
s2=PhoneBook("babbu",8108467235)

print(s1.show_contact())
print(s2.show_contact())
s1.show_all_contacts()