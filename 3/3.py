file = open('data.txt', 'r')
input = [line.strip() for line in list(file)]
file.close()

def first_part(data):
    sum = 0
    for line in data:
        common = set(line[:int(len(line)/2)]) & set(line[int(len(line)/2):])
        for letter in common:
            sum += (ord(letter) - 65 + 27 if letter.isupper() else ord(letter) - 96)
    return sum

def three_elves(data):
    common = set()
    for index in range(0,len(data)):
        common = common & set(data[index]) if len(common) else set(data[index])
    
    return sum([(ord(letter) - 65 + 27 if letter.isupper() else ord(letter) - 96) for letter in common])

def second_part(data):
    return sum([three_elves(data[index:index+3]) for index in (range(0,len(data),3))])

print("Part one:", first_part(input))
print("Part two:", second_part(input))