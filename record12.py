import pickle as p

def display():
    with open('Books.dat','rb') as f:
        data = p.load(f)
        for j in (data):
            print(f'{j}: {",".join(data[j])}')

def create():
    def create_for(f):
        data = {}
        while True:
            data[input('Book No.: ')] = [input('Title: '),input('Price: ')]
            if input('Continue? (y/n): ') == 'n':break
        p.dump(data,f)
    try:
        f = open('Books.dat','rb')
        f.close()
        confirm = True if input('ARE YOU SURE YOU WANT TO OVERWRITE? (y/n): ') == 'y' else False
        if confirm:
            f = open('Books.dat','wb')
            create_for(f)
            f.close()
        
    except FileNotFoundError:
        f = open('Books.dat','wb')
        create_for(f)
        f.close()

def update(bno):
    with open('Books.dat','rb') as f:
        data = p.load(f)
        if bno in data:
            data[bno] = [input('Title: '),input('Price: ')]
            with open('Books.dat','wb') as f:
                f.seek(0)
                p.dump(data,f)
        else:
            print('BOOK NOT FOUND')

while True:
    print('''
    1. CREATE
    2. UPDATE
    3. DISPLAY
    4. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        create()
    elif ch == 2:
        update(input('Book No.: '))
    elif ch == 3:
        display()
    elif ch == 4:
        break

