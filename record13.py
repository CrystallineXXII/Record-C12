import csv 

def display():
    with open('Employee.csv','r') as f:
        data = csv.reader(f)
        for i in data:
            print(f'{i[0]}: {i[1]}, {i[2]}')

def create():
    try:
        f = open('Employee.csv','r')
        f.close()
    except FileNotFoundError:
        f = open('Employee.csv','w')
        data = []
        while True:
            data.append([input('Emp No.: '),input('Name: '),input('Salary: '),])
            if input('Continue? (y/n): ') == 'n':break
        writer = csv.writer(f)
        writer.writerows(data)
        f.close()
