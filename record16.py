
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