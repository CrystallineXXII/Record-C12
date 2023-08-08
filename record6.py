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