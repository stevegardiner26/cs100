def readDB(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    d = {}
    for line in lines:
        d[line.split(' ')[0]] = line.split(' ')[1]

    f.close()
    print(d)


readDB('test.txt')