
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