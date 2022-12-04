file = open('data.txt', 'r')
input = [line.strip().split(",") for line in list(file)]
file.close()

def make_ID_list(elf_IDs):
    [start, end] = map(int, elf_IDs.split("-"))
    return [id for id in range(start, end + 1)]

total_overlap = 0
overlap = 0

for line in input:
    first_elf = make_ID_list(line[0])
    second_elf = make_ID_list(line[1])

    #Part one
    union = set(first_elf).union(set(second_elf))
    if len(union) == max(len(first_elf), len(second_elf)):
        total_overlap += 1
    
    #Part two
    intersection = set(first_elf).intersection(set(second_elf))
    if len(intersection) > 0:
        overlap += 1

print("Part one:", total_overlap)
print("Part two:", overlap)
