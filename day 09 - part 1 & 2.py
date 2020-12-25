import itertools
with open("C:\\Advent\\day9.txt", "r") as file:
    data = [int(x.strip()) for x in file.read().splitlines()]
    number = [data[x] for x in range(25, len(data)) if data[x] not in [sum(numbers) for numbers in itertools.combinations(data[x-25:x],2)]][0]
    print('Part 1: {}'.format(number))
    for x in range(2, len(data)):
        for i in range(len(data)):
            if sum(data[i:i+x]) == number:
                print('Part 2: {}'.format(min(data[i:i+x])+max(data[i:i+x])))
                break
        else:
            continue
        break
