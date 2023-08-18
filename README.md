# Record 1

## Q: Write a program  using functions to implement a 4 function calculator :



```py
def add(a,b): print(a+b)
def sub(a,b): print(a-b)
def mul(a,b): print(a*b)
def div(a,b): print(a/b if b != 0 else float('inf'))

while True:
    a = int(input('a: '))
    b = int(input('b: '))
    operator = input('''
(1) ADD
(2) SUB
(3) MUL
(4) DIV
''')
                     
    if   operator == '1':add(a,b)
    elif operator == '2':sub(a,b)
    elif operator == '3':mul(a,b)
    elif operator == '4':div(a,b)

    if input('Continue? (y/n): ') == 'n':break

```
---
---

# Record 2

## Q: Write a menu driven program to operate on lists :

```py
List = []
def append(elem):
    List.append(elem)
def insert(elem,pos:int):
    List.insert(pos,elem)
def delete(pos:int):
    List.pop(pos)
def extend(string:str):
    try:
        l = eval(string)
        List.extend(l)
    except (NameError,SyntaxError) as e:
        print(e)

while True:
    print(f'''
          Current list: {List}
          
          (1) Append
          (2) Insert
          (3) Delete
          (4) Extend

          ''')
    try:
        ch = int(input("Choice: "))
    
        if   ch == 1:append(int(input('Element: ')))
        elif ch == 2:insert(int(input('Element: ')),int(input('Position: ')))
        elif ch == 3:delete(int(input('Position: ')))
        elif ch == 4:extend(input('Element: '))
    
    except ValueError:
        continue

```
---
---
# Record 3

## Q: Write a program to show the statistics of a string using fuctions:

```py
def length(string:str) -> int:
    a = 0
    for i in string: 
        a += 1
    return a
 
def alpha_count(string:str) -> int:
    a = 0
    for i in string: 
        if i.isalpha():
            a += 1
    return a
 
def num_count(string:str) -> int:
    a = 0
    for i in string: 
        if i.isdigit():
            a += 1
    return a
 
def symbol_count(string:str) -> int:
    a = 0
    for i in string: 
        if not i.isalnum():
            a += 1
    return a
 
def word_count(string:str) -> int:
    a = 0
    for i in string: 
        if i.isspace():
            a += 1
    return a + 1
 
while True:
    instr = input('String: ')
    print(f'''
LENGTH OF STRING      : {length(instr)}
ALPHABETS IN STRING   : {alpha_count(instr)}
NUMBERS IN STRING     : {num_count(instr)}
SYMBOLS IN STRING     : {symbol_count(instr)}
WORDS IN STRING       : {word_count(instr)}
 
    ''')
```
---
---
# Record 4

## Q: Write a program to store the names of students in a tuple. Write functions to add and search for a name in the tuple:

```py
record = ()

def add(name):
    global record
    if name.lower().strip() in record:
        return 'CONTACT ALREADY EXISTS'
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
```
---
---
# Record 5

## Q: Write a menu driven program to implement a phonebook using dictionary:

```py
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

    if input('Continue? (y/n): ') == 'n':break
```
---
---
# Record 6

## Q: Write a program to show the words, lines and alphabets in a file:

```py
with open('poem.txt') as f:
    l = f.readlines()
    lines = len(l)
    words = sum([len(i.split()) for i in l])
    alphas = 0
    f.seek(0)
    for i in f.read():
        for j in i:
            if j.isalpha():
                alphas += 1

print(f'''
LINES     : {lines}
WORDS     : {words}
ALPHABETS : {alphas}
''')
```
---
---
# Record 7

## Q: Write a program to display the no of lines starting with a 'The' in a file:

```py
def the_count(filename):
    with open(filename) as f:
        count = 0
        for i in f.readlines():
            if i.startswith('The'):
                count += 1
        return count

print(f'The number of line starting with \'the\' in lines.txt : {the_count("lines.txt")}')
```
---
---
# Record 8

## Q: Write a program to display the no of times "he" or "she" is mentioned in a file:

```py
with open('story.txt') as f:
    s = f.read()

    he_count = s.count(' he ')
    she_count = s.count(' she ')

    print(f'''
    HE  : {he_count}
    SHE : {she_count}
    ''')
    
```
---
---
# Record 9

## Q: Write a program to copy all lines of a file starting with 'A' to a new file:



```py
def copy(fread,fwrite):
    with open(fread) as f:
        with open(fwrite,'w') as fw:
            l = f.readlines()
            for line in l:
                if line.startswith('A'):
                    fw.write(line)

copy('article.txt','newfile.txt')
print('EXECUTED SUCCESSFULLY...')
```
---
---

# Record 10

## Q: Create a binary file interface for the following:
 (1) Create a record  
 (2) Display all records  
 (3) Append a record  


```py
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
```
---
---
# Record 11

## Q: Create a binary file interface for the following:
 (1) Create a record 'flights.dat'  
 (2) Display all records  
 (3) Search a record  

```py
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

    
```
---
---
# Record 12

## Q: Create a binary file interface for the following:
 (1) Create a record 'books.dat'  
 (2) Display all records  
 (3) Update a record  


```py
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

```
---
---
# Record 13

## Q: Create a csv interface for the following:
 (1) Create a record 'Employee.csv' storing [Eno,Ename,Salary]  
 (2) Display all records  

```py
import csv 

def display():
    with open('Employee.csv','r') as f:
        data = csv.reader(f)
        for i in data:
            print(f'{i[0]}: {i[1]}, {i[2]}')

def create():
    def create_for(f):
        data = []
        while True:
            data.append([input('NAME: '),input('DEPARTMENT: '),input('SALARY: ')])
            if input('Continue? (y/n): ') == 'n':break
        csv.writer(f).writerows(data)
    try:
        f = open('Employee.csv','r')
        f.close()
        confirm = True if input('ARE YOU SURE YOU WANT TO OVERWRITE? (y/n): ') == 'y' else False
        if confirm:
            f = open('Employee.csv','w')
            create_for(f)
            f.close()
        
    except FileNotFoundError:
        f = open('Employee.csv','w')
        create_for(f)
        f.close()

while True:
    print('''
    1. CREATE
    2. DISPLAY
    3. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        create()
    elif ch == 2:
        display()
    elif ch == 3:
        break

```
---
---
# Record 14

## Q: Create a csv interface for the following:
 (1) Create a record 'Sports.csv' storing [Sport, Competitions, Prizes Won]  
 (2) Display all records  
 (3) Search a record  

```py
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
```
---
---
# Record 15

## Q: Create an interface an integer stack:

```py
stack = []

def pop():
    return stack.pop()

def push(val):
    stack.append(val)

def display():
    print(stack)

def peek():
    return stack[-1]

while True:
    print('''
    1. PUSH
    2. POP
    3. PEEK
    4. DISPLAY 
    5. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        push(input('ENTER VALUE TO PUSH: '))
    elif ch == 2:
        print(pop())
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
```
---
---
# Record 16

## Q: Create an interface a stack containing [Eno, Ename, Salary]:

```py
stack = []

def pop():
    return stack.pop()

def push(data):
    stack.append(data)

def display():
    for i in stack:
        print(f'{i[0]}: {i[1]}, {i[2]}')

def peek():
    return stack[-1]

while True:
    print('''
    1. PUSH EMPLOYEE
    2. POP EMPLOYEE
    3. PEEK EMPLOYEE
    4. DISPLAY EMPLOYEES
    5. EXIT
    ''')
    ch = int(input('ENTER YOUR CHOICE : '))
    if ch == 1:
        push([input('NO: '),input('NAME: '),input('SALARY: ')])
    elif ch == 2:
        data = pop()
        print(f'POPPED EMPLOYEE: {data[0]}: {data[1]}, {data[2]}')
    elif ch == 3:
        data = peek()
        print(f'PEEKED EMPLOYEE: {data[0]}: {data[1]}, {data[2]}')
    elif ch == 4:
        display()
    elif ch == 5:
        break
```
---