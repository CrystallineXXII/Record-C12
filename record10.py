import pickle as p

def display():
    with open('Student.dat','rb') as f:
        l = []
        try:

            while True:
                l.append(p.load(f))
        except EOFError:
            pass

        for i in l:
            print(f'''
ROLL NO : {i[0]}
NAME    : {i[1]}
MARKS   : {i[2]}''')


def create():
    def create_for(f):
        while True:
            roll = int(input('ROLL NO: '))
            name = input('NAME: ')
            marks = int(input('MARKS: '))
            data = [roll,name,marks]
            p.dump(data,f)
            if input('Continue? (y/n): ') == 'n':
                break
    try:
        f = open('Student.dat','rb')
        f.close()
        confirm = True if input('ARE YOU SURE YOU WANT TO OVERWRITE? (y/n): ') == 'y' else False
        if confirm:
            f = open('Student.dat','wb')
            create_for(f)
            f.close()

    except FileNotFoundError:
        f = open('Student.dat','wb')
        create_for(f)
        f.close()

def append(data):
    with open('Student.dat','ab') as f:
        p.dump(data,f)

while True:
    print('''
    1. CREATE
    2. APPEND
    3. DISPLAY
    4. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        create()
    elif ch == 2:
        data = [int(input('ROLL : ')),input('NAME : '),int(input('MARKS : '))]
        append(data)
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print('INVALID CHOICE...')