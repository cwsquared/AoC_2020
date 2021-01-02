from math import prod

from input_prep import file_to_str_list
from results_out import solved


def get_tree_count(tree_map, slope, tree_char, start_x, start_y):
    tree_count = 0
    tree = tree_char
    x_pos, y_pos = start_x, start_y

    while y_pos < len(tree_map):
        length = len(tree_map[y_pos])
        x_pos += slope[0]
        y_pos += slope[1]

        x_pos = x_pos - length if x_pos >= length else x_pos  # mock tree pattern to the right

        if y_pos < len(tree_map) and tree_map[y_pos][x_pos] == tree:
            tree_count += 1
            
    return tree_count


def part1(data):
    part = "1"

    tree = "#"
    tree_count, x_pos, y_pos = 0, 0, 0
    slope = (3,1)  # (to the right, and down)

    tree_count = get_tree_count(data, slope, '#', 0, 0)

    solved(day, part, tree_count)


def part2(data):
    part = "2"
    
    tree_count, x_pos, y_pos = 0, 0, 0
    tree_counts = []
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

    for slope in slopes:
        tree_counts.append(get_tree_count(data, slope, '#', 0, 0))

    solved(day, part, prod(tree_counts))


if __name__ == "__main__":
    day = "3"
    
    data = file_to_str_list("input03.txt")
    
    part1(data)
    part2(data)