import copy, math
with open("C:\\Advent\\day24.txt", 'r') as file:
    data = [x.strip() for x in file.read().splitlines()]
    instructions = []
    for x in data:
        instruction, i = [], 0
        while i < len(x):
            if x[i] in ['n','s']:
                instruction.append(x[i:i+2])
                i+= 2
            else:
                instruction.append(x[i])
                i+=1
        instructions.append(instruction[:])
    times = int(math.ceil(100/len(max(instructions))))+2
    floor = [[0 for x in range(-len(max(instructions)*times), len(max(instructions)*times)+1)] for y in range(-len(max(instructions)*times), len(max(instructions)*times)+1)]
    start = [len(max(instructions))*times, len(max(instructions))*times]
    move = {'w': lambda a: (a[0] + 2, a[1]), 'e': lambda a: (a[0] - 2, a[1]), 'nw': lambda a: (a[0] + 1, a[1] + 1), 'ne': lambda a:  (a[0] - 1, a[1] + 1), 'sw': lambda a: (a[0] + 1, a[1] - 1), 'se': lambda a: (a[0] - 1, a[1] - 1)}
    for instruction in instructions:
        current = start
        for step in instruction:
            current = move[step](current)
        floor[current[1]][current[0]] = (1 if floor[current[1]][current[0]] == 0 else 0)
    print('Part 1: {}'.format(sum([x for x in sum(floor, [])])))
    for i in range(100):
        newfloor = copy.deepcopy(floor)
        for y in range(2, len(floor)-2):
            for x in range(2+(y%2), len(floor)-(2+(y%2)), 2):
                count = 0
                for z in move.values():
                    a, b = z([x,y])
                    if floor[b][a] == 1:
                        count+=1
                if floor[y][x] == 1:
                    if count == 0 or count > 2:
                        newfloor[y][x] = 0
                else:
                    if count == 2:
                        newfloor[y][x] = 1
        floor = copy.deepcopy(newfloor)
    print('Part 2: {}'.format(sum([x for x in sum(floor, [])])))
