phoneBook = {
    'john'     :  8876773583,
    'james'    :  9989786799,
    'nicole'   :  7857674999,
             }

def add_contact(name:str,number:int):
    if name.lower() in phoneBook:
        return 'CONTACT ALREADY EXISTS'
    else:
        phoneBook[name.lower()] = number
        return 'SUCCESS'

def modify_contact(name:str,newnum:int):
    if name.lower() in phoneBook:
        phoneBook[name.lower()] = newnum
        return 'SUCCESS'
    else:
        return 'CONTACT DOES NOT EXIST'
    
def search(name:str):
    if name.lower() in phoneBook:
        return phoneBook[name.lower()]
    else:
        return 'COULD NOT FIND CONTACT'
    
def delete_contact(name:str):
    if name.lower() in phoneBook:
        del phoneBook[name.lower()]
        return 'SUCCESS'
    else:
        return 'CANNOT DELETE NONEXISTENT CONTACT'
    
def display():
    for name in phoneBook:
        print()
        print(f'{name.capitalize()}\t:  {phoneBook[name]}')
while True:
    print('''
                PHONEBOOK
               -+-+-+-+-+-

        (1) ADD A CONTACT
        (2) MODIFY A CONTACT
        (3) DELETE A CONTACT
        (4) SEARCH FOR A CONTACT
        (5) VIEW ALL CONTACTS
    ''')

    ch = int(input('Enter your choice: '))
    if   ch == 1:print(add_contact(input('Name: '),int(input('Number:'))))
    elif ch == 2:print(modify_contact(input('Name: '),int(input('New Number: '))))
    elif ch == 3:print(delete_contact(input('Name: ')))
    elif ch == 4:print(search(input('Name: ')))
    elif ch == 5: display()