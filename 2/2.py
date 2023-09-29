path = 'input.txt'

l = [int(num) for row in open(path, 'r') for num in row.strip().split(',')]

def part1(list):
    """ part 1 """
    list2 = list.copy()
    return getRes(list2, 12, 2)
    
def part2(list):
    """ part 2 """
    output = 19690720

    for noun in range(0, 99 + 1):
        for verb in range(0, 99 + 1):
            list2 = list.copy()
            if getRes(list2, noun, verb) == output:
                return 100 * noun + verb
    
    return -1

def getRes(list, noun, verb):
    list[1] = noun
    list[2] = verb

    for i in range (0, len(list), 4):
        if list[i] == 1:
            list[list[i + 3]] = list[list[i+1]] + list[list[i+2]]
        elif list[i] == 2:
            list[list[i + 3]] = list[list[i+1]] * list[list[i+2]]
        else:
            break
    
    return list[0]

print(part1(l))
print(part2(l))