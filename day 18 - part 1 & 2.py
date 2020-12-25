def calculate(eq, tot=0, p2=False):
    def calc(numbers, tot):
        if p2:
            numbers2 = []
            for e in range(0, len(numbers), 2):
                if e+2 < len(numbers):
                    if numbers[e+1] == '*':
                        numbers2 += [tot, numbers[e+1]]
                        tot = numbers[e+2]
                    else:
                        tot += numbers[e+2]
            numbers = [x for x in numbers2] + [tot]
            tot = numbers[0]
        for e in range(0, len(numbers), 2):
            if e+2 < len(numbers):
                tot = tot+numbers[e+2] if numbers[e+1] == '+' else tot*numbers[e+2]
        return eq[i+1:], tot, -1
    numbers, i = [], 0
    while i < len(eq):
        if eq[i] == '(':
            eq, val, i = calculate(eq[i+1:], p2=p2)
            numbers.append(val)
        elif eq[i] == ' ':
            if eq[:i].isalnum():
                numbers.append(int(eq[:i]))
            elif eq[:i] in ['+','*']:
                numbers.append(eq[i-1:i])
            eq, i = eq[i+1:], -1      
        elif eq[i] == ')':
            if eq[:i].isalnum():
                numbers.append(int(eq[:i]))
            return calc(numbers, numbers[0])
        i += 1
    return calc(numbers, numbers[0])[1]
                
with open("C:\\Advent\\day18.txt", 'r') as file:
    data = [x.strip()+' ' for x in file.read().splitlines()]
    print('Part 1: {}'.format(sum([calculate(x) for x in data])))
    print('Part 2: {}'.format(sum([calculate(x, p2 = True) for x in data])))
