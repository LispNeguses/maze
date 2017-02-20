import random

#gaps need to be flatenned to avoid incremental growth of the gap
def flatten_adjacent_gaps(line):
    i = 1
    while i < len(line):
        if line[i] == line[i-1] and line[i] == ' ':
            rand = random.choice([0,1])
            line[i-rand] = ''
        i += 1
    return line

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

    num_to_remove = len(gap_indexes) - 2

    for _ in range(num_to_remove):
        gap_to_remove = random.choice(gap_indexes)
        new_line[gap_to_remove] = ''


    #fill the rest of the line with either new gaps or walls
    #should they be equally likely?
    for i in range(len(new_line)):
        if new_line[i] == '':
            new_line[i] = '#'
        #generate a random map element
        tile = random.choice(['#', ' '])

        #if the newly generated element is a gap element, make sure it connects to one of the compulsory ones
        if tile == ' ':
            if i == 0:
                if new_line[i+1] == ' ':
                    new_line[i] = ' '
            elif i == (len(new_line) - 1):
                if new_line[i-1] == ' ':
                    new_line[i] = ' '
            else:
                if new_line[i-1] == ' ' or new_line[i+1] == ' ':
                    new_line[i] = ' '

    assert(len(new_line) == len(old_line))
    return new_line

def generate_test_map(initial):
    map1 = [initial]
    for i in range(25):
        map1.append(generate_level_line(map1[i]))
    return map1
