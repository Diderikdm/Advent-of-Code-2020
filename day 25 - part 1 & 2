with open("C:\\Advent\\day25.txt", 'r') as file:
    data = [int(x) for x in file.read().splitlines()]
    i, loops, value, sn = 0, {x: None for x in data}, 1, 7
    while any([x is None for x in loops.values()]):
        value = (value*sn)%20201227
        i+=1 
        if value in data:
            loops[value] = i
    sn, val, value = [k for k in loops.keys() if k != value][0], value, 1
    for i in range(loops[val]):
        value = (value*sn)%20201227
    print('Part 1: {}'.format(value))
