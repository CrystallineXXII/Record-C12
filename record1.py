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

    