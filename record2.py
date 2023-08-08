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
