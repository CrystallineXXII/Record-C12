def the_count(filename):
    with open(filename) as f:
        count = 0
        for i in f.readlines():
            if i.startswith('The'):
                count += 1
        return count

print(f'The number of line starting with \'The\' in lines.txt : {the_count("lines.txt")}')