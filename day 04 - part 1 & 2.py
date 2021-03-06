ok = {
    'byr':[1920,2002],
    'iyr':[2010,2020],
    'eyr':[2020,2030],
    'hgt':{
        'cm':[150,193],
        'in':[59,76]
        },
    'hcl':'#abc123',
    'ecl':['amb','blu','brn','gry','grn','hzl','oth'],
    'pid':'000000001'
    }

with open('C:\\Advent\\day4.txt', 'r') as file:
    data = [' '.join(x.split('\n')) for x in file.read().split('\n\n')]
    c1=0
    c2=0
    for x in data:
        vals = {y.split(':')[0]:y.split(':')[1] for y in x.split(' ')}
        if len([z for z in ok.keys() if z in vals.keys()]) == 7:
            c1 += 1
            if unicode(vals['byr'], 'utf-8').isnumeric() and len(vals['byr']) == 4 and ok['byr'][0] <= int(vals['byr']) <= ok['byr'][1] \
            and unicode(vals['iyr'], 'utf-8').isnumeric() and len(vals['iyr']) == 4 and ok['iyr'][0] <= int(vals['iyr']) <= ok['iyr'][1] \
            and unicode(vals['eyr'], 'utf-8').isnumeric() and len(vals['eyr']) == 4 and ok['eyr'][0] <= int(vals['eyr']) <= ok['eyr'][1] \
            and vals['hgt'].isalnum() and vals['hgt'][-2:] in ok['hgt'].keys() and unicode(vals['hgt'][:-2], 'utf-8').isnumeric() and \
                ok['hgt'][vals['hgt'][-2:]][0] <= int(vals['hgt'][:-2]) <= ok['hgt'][vals['hgt'][-2:]][1] \
            and vals['hcl'].startswith('#') and len(vals['hcl']) == 7 and vals['hcl'][1:].isalnum() \
            and vals['ecl'].isalpha() and len(vals['ecl']) == 3 and vals['ecl'].islower() and vals['ecl'] in ok['ecl'] \
            and unicode(vals['pid'], 'utf-8').isnumeric() and len(vals['pid']) == 9:
                c2 += 1                
    print ('Part 1: {}'.format(c1))
    print ('Part 2: {}'.format(c2))
