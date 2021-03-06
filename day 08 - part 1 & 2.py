def run_instruction(x):
    global acc
    operator, offset = x.split(' ')
    if operator == 'jmp':
        return int(offset)
    else:
        acc += int(offset) if operator == 'acc' else 0
        return 1

def find_data(data):
    global acc
    acc = 0
    indexes = [0]
    i = 0
    while i < len(data):
        offset = run_instruction(data[i])
        if not i+offset in indexes:
            indexes.append(i+offset)
        else:
            return acc, False
        i+=offset
    return acc, True

with open("C:\\Advent\\day8.txt", "r") as file:
    data = [x.strip() for x in file.read().splitlines()]
    print('Part 1: {}'.format(find_data(data)[0]))
    alter = [index for index in range(len(data)-1) if data[index].split(' ')[0] in ['jmp','nop']]
    for x in alter:
        if find_data(data[:x] + [data[x].replace('nop','jmp') if data[x].split(' ')[0] == 'nop' else data[x].replace('jmp','nop')] + data[x+1:])[1]:
            print('Part 2: {}'.format(acc))
