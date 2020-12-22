def play_recursive(p_1, p_2, one=False, two=False):
    previous = []
    while min(len(p_1),len(p_2)) > 0:
        if [p_1,p_2] in previous:
            return p_1, p_2, True, False
        previous.append([p_1[:], p_2[:]])
        a, b = p_1.pop(0), p_2.pop(0)
        if len(p_1) >= a and len(p_2) >= b:
            void, void, one, two = play_recursive(p_1[:a], p_2[:b])
            if one:
                p_1 += [a,b]
            elif two:
                p_2 += [b,a]
        else:
            if a>b:
                p_1 += [a,b]
            elif b>a:
                p_2 += [b,a]
    return p_1, p_2, p_1>p_2, p_2>p_1

def play(p1, p2):
    if len(p1) > len(p2):
        for x in p1[len(p2):]:
            yield (x, None)
    elif len(p2) > len(p1):
        for x in p2[len(p1):]:
            yield (None, x)
    for i in range(min(len(p1),len(p2))):
        if p1[i] > p2[i]:
            for z in ((p1[i], None), (p2[i], None)):
                yield z
        elif p2[i] > p1[i]:
            for z in ((None, p2[i]), (None, p1[i])):
                yield z
        
with open("C:\\Advent\\day22.txt", 'r') as file:
    p1, p2, p_1, p_2 = [[int(y) for y in x.split('\n')] for x in file.read().strip('Player 1:').strip('\n').split('\n\nPlayer 2:\n')]*2
    while min(len(p1),len(p2)) > 0:
        result = [[a,b] for a,b in play(p1,p2)]
        p1, p2 = [x[0] for x in result if x[0]], [x[1] for x in result if x[1]]
    print('Part 1: {}'.format(sum([(len(max(p1,p2)) - i) * max(p1,p2)[i] for i in range(len(max(p1,p2)))])))
    p_1, p_2, one, two = play_recursive(p_1, p_2)
    print('Part 2: {}'.format(sum([(len(p_1 if one else p_2) - i) * (p_1[i] if one else p_2[i]) for i in range(len(p_1 if one else p_2))])))
