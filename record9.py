def copy(fread,fwrite):
    with open(fread) as f:
        with open(fwrite,'w') as fw:
            l = f.readlines()
            for line in l:
                if line.startswith('A'):
                    fw.write(line)

copy('article.txt','newfile.txt')
print('EXECUTED SUCCESSFULLY...')