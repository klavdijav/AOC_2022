file = open('data.txt', 'r')
data = [value.strip() for value in list(file)]
file.close()

## Part one
calories_array = []
elf = 0
for calories in data:
    if calories:
        elf += int(calories)
    else: 
        calories_array.append(elf)
        elf = 0
        
print("Part one:", max(calories_array))

calories_array.sort(reverse=True)
print("Part two:", sum(calories_array[:3]))