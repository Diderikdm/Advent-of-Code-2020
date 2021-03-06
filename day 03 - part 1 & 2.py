def find_trees(data, right, down):
    return len([i for i in range(0, len(data), down) if data[i][int(i*right/down)%len(data[0])] == '#'])

with open("C:\\Advent\\day3.txt", 'r') as file:
    data = [value.strip() for value in file.read().splitlines()]
    print('Part 1: {}'.format(find_trees(data, 3, 1)))
    print('part 2: {}'.format(reduce((lambda x,y:x*y), [find_trees(data, right, down) for right, down in [(1,1),(3,1),(5,1),(7,1),(1,2)]])))
