path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        num = int(row.strip())
        l.append(num)

def part1(list):
    """ part 1 """
    sum = 0

    for num in list:
        sum += getFuel(num)

    return sum
    
def part2(list):
    """ part 2 """
    sum = 0

    for num in list:
        fuel = getFuel(num)

        while fuel > 0:
            sum += fuel
            fuel = getFuel(fuel)
    
    return sum

def getFuel(weight):
    return int(weight / 3) - 2

print(part1(l))
print(part2(l))
