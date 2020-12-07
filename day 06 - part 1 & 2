with open("C:\\Advent\\day6.txt", "r") as file:
    c=0
    data = [x.split('\n') for x in file.read().split('\n\n')]
    print('Part 1: {}'.format(reduce(lambda a,b:a+b, [len(set([v for v in reduce(lambda x,y:x+y, group)])) for group in data])))
    for group in data:
        grouped_data = reduce(lambda x,y:x+y, group)
        c += len(set(''.join([x for x in grouped_data if grouped_data.count(x) == len(group)])))
    print('Part 2: {}'.format(c))
