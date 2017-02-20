import unittest
from level import generate_level_line

class TestLevel(unittest.TestCase):
    def test_two_traversable_routes(self):
        level = [['#', '#', ' ', '#', '#', ' ', '#', '#', '#']]
        level.append(generate_level_line(level[0]))
        route_ct = 0
        prev_char = None
        current_gap_traversable = None

        for line in range(len(level)-1):
            for col in range(len(level[0])):
                #if a path has been found through the current gap, then skip
                if prev_char == level[line][col] and current_gap_traversable == True:
                    continue
                else:
                    current_gap_traversable = False

                if level[line][col] == ' ':
                    if level[line+1][col] == ' ':
                        route_ct += 1
                        current_gap_traversable = True
                prev_char = level[line][col]

        assert(route_ct >= 2)






if __name__ == '__main__':
    unittest.main()
