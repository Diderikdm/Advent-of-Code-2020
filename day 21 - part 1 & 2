with open("C:\\Advent\\day21.txt", 'r') as file:
    data = [x.strip() for x in file.read().splitlines()]
    allergen_data = {}
    recipes = []
    for x in data:
        if x.endswith(')'):
            ingredients, allergens = x.strip(')').split(' (contains ')
            recipes.append(ingredients.split(' '))
            for allergen in allergens.split(', '):
                if allergen not in allergen_data:
                    allergen_data[allergen] = []
                allergen_data[allergen].append(ingredients.split(' '))
        else:
            recipes.append(x.split(' '))
    combinations = {k:[] for k in allergen_data.keys()}
    for k,v in allergen_data.items():
        for ingredient in v[0]:
            if all([ingredient in x for x in v[1:]]):
                combinations[k].append(ingredient)
    found = {}
    while not all([e in found.keys() for e in allergen_data.keys()]):
        for k,v in sorted(combinations.items(), key= lambda item : len(item[1])):
            for x in found.values():
                if x in v:
                    v.remove(x)
            if len(v) == 1:
                found[k]= v[0]
    total = 0
    for recipe in recipes:
        for ingredient in recipe:
            if ingredient not in found.values():
                total += 1
    print('Part 1: {}'.format(total))
    print('Part 2: {}'.format(','.join([v for k,v in sorted(found.items(), key = lambda item: item[0])])))
