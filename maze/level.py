import random

#gaps need to be flatenned to avoid incremental growth of the gap
def flatten_adjacent_gaps(line):
    flattened_line = list(line)
    i = 1
    while i < len(flattened_line):
        if flattened_line[i] == flattened_line[i-1] and flattened_line[i] == ' ':
            rand = random.choice([0,1])
            flattened_line[i-rand] = ''
        i += 1
    return flattened_line

#returns a new line with the same length as the previous line
#assumes previous line obeys the specification, should probably add some checks
def generate_level_line(old_line):
    new_line = [tile if tile == ' ' else '' for tile in old_line]
    new_line = flatten_adjacent_gaps(new_line)

    #keep just two gaps before filling the rest of the line
    gap_indexes = []
    for i in range(len(new_line)):
        if new_line[i] == ' ':
            gap_indexes.append(i)
    num_to_delete = len(gap_indexes) - 2
    for _ in range(num_to_delete):
        index_to_delete = random.choice(gap_indexes)
        del new_line[index_to_delete]

    #fill the rest of the line with either new gaps or walls
    #should they be equally likely?
    new_line = [random.choice(['#', ' ']) if tile == '' else ' ' for tile in new_line]

    assert(len(new_line) == len(old_line))
    return new_line

