def sail(data, compass, part2=False, x=0, y=0, di=0, px=0, py=0):
    for op, val in data:
        op = op if part2 else ([d for d in compass[di].keys()][0] if op == 'F' else op)
        x += val*[d[op] for d in compass if op in d.keys()][0] if op in ['E','W'] else 0
        y += val*[d[op] for d in compass if op in d.keys()][0] if op in ['N','S'] else 0
        di = (di+int(val/90))%4 if op == 'R' else ((di-(int(val/90)))%4 if op == 'L' else di)
        if part2 and op in ['R','L']:
             for rot in range(int(val/90)%4 if op == 'R' else ((4-int(val/90))%4 if op == 'L' else 0)):
                x,y = y,-x
        px += val*x if op == 'F' else 0
        py += val*y if op == 'F' else 0
    return {'p1':[x,y],'p2':[px,py]}

with open("C:\\Advent\\day12.txt", "r") as file:
    data = [(x.strip()[0], int(x.strip()[1:])) for x in file.read().splitlines()]
    compass = [{'E':1},{'S':-1},{'W':-1},{'N':1}]
    print('Part 1: {}'.format(reduce(lambda a,b: abs(a)+abs(b), sail(data, compass)['p1'])))
    print('Part 2: {}'.format(reduce(lambda a,b: abs(a)+abs(b), sail(data, compass, part2=True, x=10, y=1)['p2'])))
