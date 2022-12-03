file = open('data.txt', 'r')
data = file.readlines()

def part_one(lines):
    score = 0
    for line in lines:
        [enemyShape, myShape] = line.strip().split(" ")
        enemyMove = ord(enemyShape) - 64
        myMove = ord(myShape) - 87

        difference = myMove - enemyMove
        if abs(difference) == 2:
            difference = myMove - (enemyMove % 3)

        score += myMove

        if difference == 0:
            score += 3
        elif difference == 1:
            score += 6
        else: 
            score += 0
    return score

def part_two(lines):
    score = 0
    for line in lines:
        [enemyShape, resultShape] = line.strip().split(" ")
        enemyMove = ord(enemyShape) - 64
        result = ord(resultShape) - 87

        if result == 1:
            score += ((enemyMove - 1) % 3 or 3)
        elif result == 2:
            score += (enemyMove + 3)
        else:
            score += (((enemyMove + 1) % 3 or 3) + 6)
    
    return score


print("Part one:", part_one(data))
print("Part two:", part_two(data))