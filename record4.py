record = ()

def add(name):
    global record
    if name.lower().strip() in record:
        return 'STUDENT ALREADY EXIST'
    else:
        record += (name.lower().strip(),)

def search(name):
    global record
    if name.lower().strip() in record:
        return 'PRESENT'
    else:
        return 'ABSENT'
    
while True:
    print(record)
    print('''
    (1) ADD
    (2) SEARCH
    ''')

    ch = int(input('Enter your choice: '))
    if   ch == 1:print(add(input('Name: ')))
    elif ch == 2:print(search(input('Name: ')))

    if input('Continue? (y/n): ') == 'n':break
    