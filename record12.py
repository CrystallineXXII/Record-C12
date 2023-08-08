import pickle as p

def display():
    with open('Books.dat','rb') as f:
        data = p.load(f)
        for j in (data):
            print(f'{j}: {",".join(data[j])}')

def create():
    try:
        f = open('Books.dat','rb')
        f.close()
    except FileNotFoundError:
        f = open('Books.dat','wb')
        data = {}
        while True:
            data[input('Book No.: ')] = [input('Title: '),input('Price: ')]
            if input('Continue? (y/n): ') == 'n':break
        p.dump(data,f)
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


