import itertools
def iterate_1(coords, mn, mx):
    mn += -1
    mx += 1
    coords.update({(x,y,z) : '.' for x in range(mn,mx+1) for y in range(mn,mx+1) for z in range(mn,mx+1)if x in [mn,mx] or y in [mn,mx] or z in [mn,mx]})
    new = coords.copy()
    for x,y,z in coords.keys():
        neighbors = [coords[(x+a,y+b,z+c)] for a,b,c in [v for v in list(itertools.product([1,0,-1], repeat=3)) if v != (0,0,0)] if (x+a,y+b,z+c) in coords and coords[(x+a,y+b,z+c)] == '#']
        if coords[(x,y,z)] == '#':
            new[(x,y,z)] = '#' if len([n for n in neighbors if n == '#']) in [2,3] else '.'
        else:
            new[(x,y,z)] = '#' if len([n for n in neighbors if n == '#']) == 3 else '.'   
    return new, mn, mx

def iterate_2(coords2, mn2, mx2):
    mn2 += -1
    mx2 += 1
    coords2.update({(x,y,z,w) : '.' for x in range(mn2,mx2+1) for y in range(mn2,mx2+1) for z in range(mn2,mx2+1) for w in range(mn2,mx2+1) if x in [mn2,mx2] or y in [mn2,mx2] or z in [mn2,mx2] or w in [mn2,mx2]})
    new = coords2.copy()
    for x,y,z,w in coords2.keys():
        neighbors = [coords2[(x+a,y+b,z+c,w+d)] for a,b,c,d in [v for v in list(itertools.product([1,0,-1], repeat=4)) if v != (0,0,0,0)] if (x+a,y+b,z+c,w+d) in coords2 and coords2[(x+a,y+b,z+c,w+d)] == '#']
        if coords2[(x,y,z,w)] == '#':
            new[(x,y,z,w)] = '#' if len([n for n in neighbors if n == '#']) in [2,3] else '.'
        else:
            new[(x,y,z,w)] = '#' if len([n for n in neighbors if n == '#']) == 3 else '.'   
    return new, mn2, mx2


with open("C:\\Advent\\day17.txt", 'r') as file:
    data = [x.strip() for x in file.read().splitlines()]
    coords = {(x,y,0) : data[y][x] for x in range(len(data)) for y in range(len(data))}
    coords.update({(x,y,z) : '.' for x in range(len(data)) for y in range(len(data)) for z in range(len(data)) if z != 0})
    mn, mx = 0, len(data)-1
    for x in range(6):
        coords, mn, mx = iterate_1(coords, mn, mx)
    print('Part 1: {}'.format(len([x for x in coords.values() if x == '#'])))
    
    coords2 = {(x,y,0,0) : data[y][x] for x in range(len(data)) for y in range(len(data))}
    coords2.update({(x,y,z,w) : '.' for x in range(len(data)) for y in range(len(data)) for z in range(len(data)) for w in range(len(data)) if not (z == 0 and w == 0)})
    mn2, mx2 = 0, len(data)-1
    for x in range(6):
        coords2, mn2, mx2 = iterate_2(coords2, mn2, mx2)
    print('Part 2: {}'.format(len([x for x in coords2.values() if x == '#'])))









# Generic function for part 1&2:
'''

import itertools
def iterate(coords, mn, mx, iterator):
    mn += -1
    mx += 1
    a = {tuple(t for t in e) : '.' for e in [v for v in list(itertools.product([i for i in range(mn,mx+1)], repeat=iterator)) if not all([s == 0 for s in v]) and any([x for x in v if x in [mn,mx]])]}
    coords.update({tuple(t for t in e) : '.' for e in [v for v in list(itertools.product([i for i in range(mn,mx+1)], repeat=iterator)) if not all([s == 0 for s in v]) and any([x in [mn,mx] for x in v])]})
    new = coords.copy()
    for key in coords.keys():
        neighbors = [coords[tuple(key[i]+e[i] for i in range(iterator))] for e in [v for v in list(itertools.product([1,0,-1], repeat=iterator)) if not all([s == 0 for s in v])] \
                     if tuple(key[i]+e[i] for i in range(iterator)) in coords and coords[tuple(key[i]+e[i] for i in range(iterator))] == '#']
        if coords[tuple(key[i] for i in range(iterator))] == '#':
            new[tuple(key[i] for i in range(iterator))] = '#' if len([n for n in neighbors if n == '#']) in [2,3] else '.'
        else:
            new[tuple(key[i] for i in range(iterator))] = '#' if len([n for n in neighbors if n == '#']) == 3 else '.'   
    return new, mn, mx

def run(data, iterator):
    coords = {(x,y)+tuple(0 for i in range(iterator-2)) : data[y][x] for x in range(len(data)) for y in range(len(data))}
    start = [v for v in list(itertools.product([i for i in range(len(data))], repeat=iterator)) if not all([s == 0 for s in v])]
    coords.update({tuple(x for x in v) : '.' for v in start if not all([s == 0 for s in list(v)[2:]])})
    mn, mx = 0, len(data)-1
    for x in range(6):
        coords, mn, mx = iterate(coords, mn, mx, iterator)
    return coords

with open("C:\\Advent\\day17.txt", 'r') as file:
    data = [x.strip() for x in file.read().splitlines()]
    print('Part 1: {}'.format(len([x for x in run(data, 3).values() if x == '#'])))
    print('Part 2: {}'.format(len([x for x in run(data, 4).values() if x == '#'])))'''
