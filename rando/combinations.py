
def generate_sets(n):
    args = [i+1 for i in range(n)]
    all_sets = []
    result = [0 for i in range(n)]
    __generate_combinations(args, 0, 0, all_sets, result)
    print(len(args))
    return all_sets


def __generate_combinations(args, start, pos, all_sets, result):
    if pos == len(args):
        return
    new_set = create_set(result, pos)
    all_sets.append(new_set)
    for i in range(start,len(args)):
        result[pos] = args[i]
        __generate_combinations(args, i + 1, pos + 1, all_sets, result)


def create_set(result, pos):
    if pos == 0:
        return set()
    return {result[i] for i in range(pos)}

print(sorted(generate_sets(3)))