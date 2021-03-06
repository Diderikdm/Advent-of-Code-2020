with open("C:\\Advent\\day1.txt", 'r') as file:
    data = [int(value) for value in file.read().splitlines()]
    print('Part 1: {}'.format([x*y for x in data for y in data if x+y == 2020][0]))
    print('Part 2: {}'.format([x*y*z for x in data for y in data for z in data if x+y+z == 2020][0]))
