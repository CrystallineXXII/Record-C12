import pickle as p

def display():
    with open('Student.dat','rb') as f:
        l = []
        try:

            while True:
                l.append(p.load(f))
        except EOFError:
            pass

        s = '\n'.join(l)
        print(s)

def create():
    try:
        f = open('Student.dat','wb')
        f.close()
    except FileNotFoundError:
        f = open('Student.dat','x')
        return f

def append(data):
    with open('Student.dat','ab') as f:
        p.dump(data,f)