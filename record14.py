import csv 

def display():
    with open('Sports.csv','r') as f:
        data = csv.reader(f)
        for i in data:
            print(f'{i[0]}: {i[1]}, {i[2]}')

def create():
    def create_for(f):
        data = []
        while True:
            data.append([input('SPORT: '),input('COMPETITION: '),input('PRIZES: ')])
            if input('Continue? (y/n): ') == 'n':break
        csv.writer(f).writerows(data)
    try:
        f = open('Sports.csv','r')
        f.close()
        confirm = True if input('ARE YOU SURE YOU WANT TO OVERWRITE? (y/n): ') == 'y' else False
        if confirm:
            f = open('Sports.csv','w')
            create_for(f)
            f.close()
        
    except FileNotFoundError:
        f = open('Sports.csv','w')
        create_for(f)
        f.close()

def search(sport):
    with open('Sports.csv','r') as f:
        data = csv.reader(f)
        for i in data:
            if sport == i[0]:
                print(f'{i[0]}: {i[1]}, {i[2]}')
while True:
    print('''
    1. CREATE
    2. DISPLAY
    3. SEARCH
    4. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        create()
    elif ch == 2:
        display()
    elif ch == 3:
        search(input('SPORT: '))
    elif ch == 4:
        break