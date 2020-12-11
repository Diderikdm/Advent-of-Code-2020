from copy import deepcopy

def find_adjescent(newdata, x, y, adjescents=0):
    for a,b in adjescent_indexes:
        for i in range(1,len(newdata)):
            if miny <= y+a*i <= maxy and minx <= x+b*i <= maxx:
                if newdata[y+a*i][x+b*i] == empty:
                    break
                elif newdata[y+a*i][x+b*i] == vacant:
                    adjescents += 1
                    break
    return adjescents
    
def rearrange(data, newdata, part2=False):
    max_occ = 5 if part2 else 4
    while data != newdata:
        newdata = deepcopy(data)
        for y in range(0, len(data)):
            for x in range(0, len(data[y])):
                if newdata[y][x] == floor:
                    continue
                adjescents = find_adjescent(newdata, x, y) if part2 else len([newdata[y+a][x+b] for a,b in adjescent_indexes if miny <= y+a <= maxy and minx <= x+b <= maxx and newdata[y+a][x+b] == vacant])
                if newdata[y][x] == empty and adjescents == 0:
                    data[y][x] = vacant
                elif adjescents >= max_occ:
                    data[y][x] = empty
    return data

with open("C:\\Advent\\day11.txt", "r") as file:
    data, newdata = [[y for y in x.strip()] for x in file.read().splitlines()], []
    vacant, empty, floor = '#', 'L', '.'
    minx, miny, maxx, maxy = 0, 0, len(data[0])-1, len(data)-1
    adjescent_indexes = [[[-x,-x],[-x,0],[-x,x],[0,x],[x,x],[x,0],[x,-x],[0,-x]] for x in range(-1,1) if x != 0][0]
    print('Part 1: {}'.format(sum(x.count(vacant) for x in rearrange(deepcopy(data), newdata))))
    print('Part 2: {}'.format(sum(x.count(vacant) for x in rearrange(data, newdata, part2=True))))
