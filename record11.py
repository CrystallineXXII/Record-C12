import pickle as p

def display():
    with open('Flights.dat','rb') as f:
        data = p.load(f)
        for i in data:
            print(f'{i}: {data[i][0]}, {data[i][1]}, ({data[i][2]})')

def create():
    try:
        f = open('Flights.dat','rb')
        f.close()
    except FileNotFoundError:
        f = open('Flights.dat','wb')
        data = {}
        while True:
            data[input('Flight No.: ')] = [input('Destination: '),input('Departure: '),input('Arrival: ')]
            if input('Continue? (y/n): ') == 'n':break
        p.dump(data,f)
        f.close()

def search(fno):
    with open('Flights.dat','rb') as f:
        data = p.load(f)
        if fno in data:
            print(f'{fno}: {data[fno][0]}, {data[fno][1]}, ({data[fno][2]})')
        else:
            print('FLIGHT NOT FOUND')
    
