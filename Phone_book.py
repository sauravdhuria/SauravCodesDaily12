class PhoneBook:
    phone_contact=[] #store contact information #class variable
                    # (shared to instance&class methods)
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

        PhoneBook.phone_contact.append(self)

    #instance method for showing contacts
    """
    
    instance because it is bound to object 
    
    """

    def show_contact(self):

        return F"Name of contact: {self.name} ,Phone Number: {self.phone_number}"  # Only 1 contact is
            # displayed which is bound to object

    """
    To get all the contact at one go we need to use class method
    """

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_contact)==0:
            print("No contact found in the phone book")
        else :
            print("All contacts from the directory !!")
            for contact in cls.phone_contact:
                print(contact.show_contact())
                                                #each contact is a object using dot operator to use objects
    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_contact:
            if contact.name == search_name:
                return print(f"Contact found name :{contact.name} , NUmber: {contact.phone_number}")

        return print(f"No contact found with name : {search_name}")

    """
    static methods are methods that are not bound to class or object
    i will use static method to validate contacts \
    """
    @staticmethod
    def validate_contact(phone_number):
        if len(phone_number) >= 8 and phone_number.isdigit():#is digit fun is used on string to check all
                                                    # CHARACTER IN STRING ARE DIGIT
            return True
        else:
            return False



no_of_contact=int(input("How many contacts you want to add :"))
for i in range(no_of_contact):
    name = input("Enter Name of contact: ")
    phone_number = input("Enter Phone Number : ")
    if PhoneBook.validate_contact(phone_number):
        PhoneBook(name,phone_number)
    else:
        print(f"Invalid contact {name} : {phone_number} ,phone number must be 8 digits")

PhoneBook.show_all_contacts()
# s2=PhoneBook("babbu",8108467235)
#

# s1.search_contact("babbu")
# s1.search_contact("Saurav")
# s1.search_contact("dbabbu")
