with open("C:\\Advent\\day2.txt", 'r') as file:
    data = [value for value in file.read().splitlines()]
    c1=0
    c2=0
    for x in data:
        k,v = x.split(':')
        first_val, second_val = k.split(' ')[0].split('-')
        if int(first_val) <= len([x for x in v.strip() if x == k[-1]]) <= int(second_val):
            c1+=1
        if (v[int(first_val)] == k[-1]) != (v[int(second_val)] == k[-1]):
            c2+=1
    print('Part 1: {}'.format(c1))
    print('Part 2: {}'.format(c2))
