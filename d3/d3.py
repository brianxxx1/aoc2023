from itertools import groupby
from operator import itemgetter


def find_sum_of_parts(input:str):
    data_line = input.split("\n")
    sum = 0
    for line_index, data in enumerate(data_line):
        indexes_of_nums = get_indexes_of_digits(data)
        for indexes in indexes_of_nums:
            sum += check_neighbour(indexes=indexes, row=line_index, data_line=data_line)
    print(sum)


def check_neighbour(indexes: list, row: int, data_line: list):
    # Directions: up, left, right, down
    directions = [(-1, 0),(-1 ,-1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
    flag = False
    for index in indexes:
        for dr, dc in directions:
            new_row, column = row + dr, index + dc
            try:
                if not data_line[new_row][column].isdigit() and data_line[new_row][column] != ".":
                    flag = True
                    break
                else:
                    continue
            except IndexError:
                pass
    if flag:
        string = ""
        for index in indexes:
            string += data_line[row][index]
        return int(string)
    else:
        return 0


def get_indexes_of_digits(data:str) -> list:
    lst = []
    for index, value in enumerate(data):
        if value.isdigit():
            lst.append(index)
    # First, sort the list to ensure numbers are in order
    lst.sort()

    # Group continuous numbers together
    grouped = []
    for k, g in groupby(enumerate(lst), lambda x: x[0] - x[1]):
        grouped.append(list(map(itemgetter(1), g)))

    return grouped

def part_2(data):
    data_lines = data.split("\n")
    indexes_of_nums = []
    for data_line in data_lines:
        indexes_of_nums.append(get_indexes_of_digits(data_line))

    sum = 0
    for line_index, data_line in enumerate(data_lines):
        for index, element in enumerate(data_line):
            if element == "*":
                directions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
                indexes_set = set()
                for dr, dc in directions:
                    new_row, column = line_index + dr, index + dc
                    for item in indexes_of_nums[new_row]:
                        if column in item:
                            indexes_set.add((new_row,tuple(item)))
                if len(indexes_set) == 2:
                    lst = get_num(indexes_set, data_lines)
                    sum += lst[0] * lst[1]
    print(sum)
def get_num(indexes_set, data_lines):
    num_list = []
    for set in indexes_set:
        str = ""
        for index in set[1]:
            str += data_lines[set[0]][index]
        num_list.append(int(str))
    return num_list

with open("input.txt") as f:
    data = f.read()
    part_2(data)
