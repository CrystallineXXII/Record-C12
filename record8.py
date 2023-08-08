with open('story.txt') as f:
    s = f.read()

    he_count = s.count(' he ')
    she_count = s.count(' she ')

    print(f'''
    HE  : {he_count}
    SHE : {she_count}
    ''')
    

