with open('data.txt') as file:
    string = file.readline()
    print("Part one:", next(i for i in range(len(string)-3) if len(set(string[i:i+4])) == 4))
    print("Part two:", next(i for i in range(len(string)-3) if len(set(string[i:i+14])) == 14))