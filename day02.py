import re

from input_prep import file_to_str_list
from results_out import solved


def part1(data):
    part = "1"

    valid_count = 0
    p = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]*)")
    for i in data:
        m = p.match(i)
        lower_bound = int(m.group(1))
        upper_bound = int(m.group(2))
        check_char = m.group(3)
        password = m.group(4)
        if lower_bound <= password.count(check_char) <= upper_bound:
            valid_count += 1
    solved(day, part, valid_count)


def part2(data):
    part = "2"
    valid_count = 0

    p = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]*)")
    for i in data:
        m = p.match(i)
        first_pos = int(m.group(1)) - 1
        second_pos = int(m.group(2)) - 1
        check_char = m.group(3)
        password = m.group(4)
        if ((password[first_pos] == check_char) ^ (password[second_pos] == check_char)):
            valid_count += 1
    solved(day, part, valid_count)


if __name__ == "__main__":
    day = "2"
    
    data = file_to_str_list("input02.txt")
    
    part1(data)
    part2(data)