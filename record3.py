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
