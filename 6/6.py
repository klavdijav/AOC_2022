with open('data.txt') as file:
    string = file.readline()
    print("Part one:", next(i for i in range(len(string)) if len(set(string[i-4:i])) == 4))
    print("Part two:", next(i for i in range(len(string)) if len(set(string[i-14:i])) == 14))