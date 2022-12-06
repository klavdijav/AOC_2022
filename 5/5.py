import re

file = open('data.txt', 'r')
input = [line.replace("\n", "") for line in list(file)]
file.close()

def move_container(num, from_line, to_line, cargo, is_lifo):
    containers_to_move = []
    for row in cargo:
        for container in row[from_line - 1]:
            if container != "" and len(containers_to_move) < num:
                containers_to_move.append(container)
                row[from_line - 1] = ""

    for index in range(len(cargo)-1, -1, -1):
        if cargo[index][to_line-1] == "" and len(containers_to_move):
            cargo[index][to_line-1] = containers_to_move.pop() if is_lifo else containers_to_move.pop(0)

    while len(containers_to_move) != 0:
        cargo.insert(0, ["" for _ in range(len(cargo[0]))])
        cargo[0][to_line - 1] = containers_to_move.pop() if is_lifo else containers_to_move.pop(0)

    return cargo
    
def run_instructions(instructions, cargo, is_lifo):
    for line in instructions:
        num, from_line, to_line = map(int, re.findall(r"\d+", line))
        cargo = move_container(num, from_line, to_line, cargo, is_lifo)

    return get_message(cargo)

def get_message(cargo):
    message = ["" for _ in cargo[0]]

    for row_index in range(len(cargo)):
        for column_index in range(len(message)):
            if message[column_index] == "" and cargo[row_index][column_index] != "":
                message[column_index] = cargo[row_index][column_index]
    
    return "".join(message)
    

def rearrange_cargo(is_lifo): 
    for index, line in enumerate(input):
        if line.strip() == "":
            cargo = [re.findall(r"\[(.*?)\]", line.replace("    ", "[]").replace(" ", "")) for line in input[:index-1]]
            return run_instructions(input[index+1:], cargo, is_lifo)

print("Part one:", rearrange_cargo(True))
print("Part two:", rearrange_cargo(False))