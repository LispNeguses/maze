import random

def flatten_adjacent_gaps(old_line):
    """Flattens gaps to avoid incremental growth of gaps"""
    line = list(old_line)
    i = 1
    current_gap_matches = 0
    prev_gap_matches = 0
    while i < len(line):
        if line[i] == line[i-1] and line[i] != '#':
            current_gap_matches += 1
        else:
            current_gap_matches = 0
        if i == len(line) - 1 and current_gap_matches > 0:
            new_i = i + 1
            gap_size = current_gap_matches + 1
            final_merged_gap_index = random.choice(range(gap_size))
            for j in range(new_i-gap_size, new_i):
                if j == new_i - final_merged_gap_index-1:
                    line[j] = ' '
                else:
                    line[j] = '#'

        elif current_gap_matches == 0 and prev_gap_matches > 0:
            gap_size = prev_gap_matches + 1
            final_merged_gap_index = random.choice(range(gap_size))
            for j in range(i-gap_size, i):
                if j == i - final_merged_gap_index-1:
                    line[j] = ' '
                else:
                    line[j] = '#'
        prev_gap_matches = current_gap_matches
        i += 1
    return line


def reduce_to_two_gaps(old_line):
    """There must always be at least routes, if a join occurs, create a new branch"""
    line = list(old_line)
    gap_indexes = []
    len(line)
    for i in range(len(line)):
        if line[i] == ' ':
            gap_indexes.append(i)

    if len(gap_indexes) == 2:
        return line

    elif len(gap_indexes) < 2:
        while True:
            gap_to_add_indexes = [i for i in range(len(line)) if i not in gap_indexes]
            gap_to_add_index = random.choice(gap_to_add_indexes)
            if gap_to_add_index == 0:
                if line[gap_to_add_index+1] == ' ':
                    continue
            elif gap_to_add_index == len(line) - 1:
                if line[gap_to_add_index-1] == ' ':
                    continue
            elif line[gap_to_add_index-1] == ' ' or line[gap_to_add_index+1] == ' ':
                continue
            else:
                line[gap_to_add_index] = ' '
                break

    elif len(gap_indexes) > 2:
        num_to_remove = len(gap_indexes) - 2
        for _ in range(num_to_remove):
            gap_to_remove = random.choice(gap_indexes)
            line[gap_to_remove] = '#'

    return line


def generate_level_line(old_line):
    new_line = [tile if tile == ' ' else tile for tile in old_line]
    new_line = flatten_adjacent_gaps(new_line)
    #print("flattened", new_line)

    new_line = reduce_to_two_gaps(new_line)
    #print("reduced", new_line)

    #fill the rest of the line with either new gaps or walls
    for i in range(len(new_line)):
        tile = random.choices(['#', ' '], [1, 1.3])[0]

        #make sure gaps connect
        if tile == ' ':
            if i == 0:
                if new_line[i+1] != '#':
                    new_line[i] = ' '
            elif i == (len(new_line) - 1):
                if new_line[i-1] != '#':
                    new_line[i] = ' '
            else:
                if new_line[i-1] != '#' or new_line[i+1] != '#':
                    new_line[i] = ' '

    assert(len(new_line) == len(old_line))

    #print("final", new_line, "\n")
    return new_line

def generate_test_map(initial):
    map1 = [initial]
    for i in range(25):
        map1.append(generate_level_line(map1[i]))
    return map1
