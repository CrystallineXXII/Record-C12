import pickle as p

def display():
    with open('Flights.dat','rb') as f:
        data = p.load(f)
        for i in data:
            print(f'{i}: {data[i][0]}, ({data[i][1]} - {data[i][2]})')

def create():
    def create_for(f):
        data = {}
        while True:
            data[input('Flight No.: ')] = [input('Destination: '),input('Departure: '),input('Arrival: ')]
            if input('Continue? (y/n): ') == 'n':break
        p.dump(data,f)
    try:
        f = open('Flights.dat','rb')
        f.close()
        confirm = True if input('ARE YOU SURE YOU WANT TO OVERWRITE? (y/n): ') == 'y' else False
        if confirm:
            f = open('Flights.dat','wb')
            create_for(f)
            f.close()
        
    except FileNotFoundError:
        f = open('Flights.dat','wb')
        create_for(f)
        f.close()

def search(fno):
    with open('Flights.dat','rb') as f:
        data = p.load(f)
        if fno in data:
            print(f'{fno}: {data[fno][0]}, ({data[fno][1]} - {data[fno][2]})')
        else:
            print('FLIGHT NOT FOUND')
    
while True:
    print('''
    1. CREATE
    2. SEARCH
    3. DISPLAY
    4. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        create()
    elif ch == 2:
        search(input('Flight No.: '))
    elif ch == 3:
        display()
    elif ch == 4:
        break
