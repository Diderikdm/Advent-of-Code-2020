import itertools
with open("C:\\Advent\\day14.txt", "r") as file:
    data = [x.strip() for x in file.read().splitlines()]
    mem, mem_p2 = {}, {}
    for x in data:
        if x.startswith('mask'):
            mask = x.split(' = ')[1]
        else:
            index = int(x.split('[')[1].split(']')[0])
            intval = int(x.split(' = ')[1])
            binaryval = (36-len(format(intval, 'b')))*'0'+format(intval, 'b')
            vals = [v for v in binaryval]
            for e in [i for i in range(len(mask)) if mask[i] != 'X']:
                vals[e] = mask[e]
            mem[index] = int(''.join(vals), 2)
            binaryindex = (36-len(format(index, 'b')))*'0'+format(index, 'b')
            index_vals = [v for v in binaryindex]
            for e in [i for i in range(len(mask)) if mask[i] != '0']:
                index_vals[e] = mask[e]
            x_indexes = [i for i in range(len(mask)) if mask[i] == 'X']
            options = list(itertools.product(['1','0'], repeat=len(x_indexes)))
            for e in range(len(options)):
                for i in range(len(options[e])):
                    index_vals[x_indexes[i]] = options[e][i]
                mem_p2[int(''.join(index_vals), 2)] = intval          
    print('Part 1: {}'.format(reduce(lambda x,y: x+y, [z for z in mem.values()])))
    print('Part 2: {}'.format(reduce(lambda x,y: x+y, [z for z in mem_p2.values()])))
