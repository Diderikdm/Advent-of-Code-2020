with open("C:\\Advent\\day10.txt", "r") as file:
    data = sorted([int(x.strip()) for x in file.read().splitlines()])
    data = [0] + data + [max(data)+3]
    print('Part 1: {}'.format(len([data[x] for x in range(1, len(data)) if data[x]-data[x-1] == 1])*len([data[x] for x in range(1, len(data)) if data[x]-data[x-1] == 3])))
    paths = {data[0]:1}
    for x in data[1:]:
        paths[x] = sum(paths[x-y] for y in range(1,4) if x-y in paths)
    print('Part 2: {}'.format(paths[data[-1]]))
