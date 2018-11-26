# Phonebook app exercise

def phoneBook():
    phone_on = True;

    
    while phone_on:
        print """
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    """
        entry = raw_input("What do you want to do? (1-5) ")
        phone_book = {
            'Self' : '123-456-7890'
        }
        if entry == "5":
            print "Shutting down..."
            phone_on = False
            break;

        elif entry == "1":
            name = raw_input("Name?: ")
            print phone_book[name]
            phoneBook()
            
        elif entry == '2':
            name_entry = raw_input("Name: ")
            number_entry = raw_input('Number: ')
            phone_book.update({ name_entry : number_entry })
            print "Entry stored for %s." % name_entry
            phoneBook()
            
        elif entry == '3':
            entry_del = raw_input('contact to delete: ')
            del phone_book[entry_del]
            phoneBook()

        elif entry == '4':
            print phone_book
            phoneBook()
        
phoneBook()