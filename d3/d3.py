## Advent of Code 2023, Day 3


# Part 1 ======================================================================================================================
import re


def find_sum_of_parts(input:str) -> int:
    data_line = input.split("\n")
    parts_list = []
    for line_index, data in enumerate(data_line):
        previous_line_index = line_index - 1
        next_line_index = line_index + 1
        nums = re.findall(r'\d+', data)
        for num in nums:
            print(num)
            if previous_line_index < 0:
                pass
            else:
                indexes = find_index_of_num(num,data)
                # print(indexes)

                for index in indexes:
                    if not data_line[previous_line_index][index].isdigit() and data_line[previous_line_index][index] != ".":
                        parts_list.append(num)
                        break

                if indexes[0] - 1 > 0:
                    if not data_line[previous_line_index][indexes[0] - 1].isdigit() and data_line[previous_line_index][
                        indexes[0] - 1] != ".":
                        parts_list.append(num)
                        continue
                if indexes[-1] + 1 < len(data_line):
                    if not data_line[previous_line_index][indexes[-1] + 1].isdigit() and data_line[previous_line_index][
                        indexes[-1] + 1] != ".":
                        parts_list.append(num)
                        continue

            if next_line_index >= len(data_line):
                pass
            else:
                indexes = find_index_of_num(num, data)
                for index in indexes:
                    if not data_line[next_line_index][index].isdigit() and data_line[next_line_index][index] != ".":
                        parts_list.append(num)
                        break
                if indexes[0] - 1 > 0:
                    if not data_line[next_line_index][indexes[0] - 1].isdigit() and data_line[next_line_index][
                        indexes[0] - 1] != ".":
                        parts_list.append(num)
                        continue
                if indexes[-1] + 1 < len(data_line):
                    if not data_line[next_line_index][indexes[-1] + 1].isdigit() and data_line[next_line_index][
                        indexes[-1] + 1] != ".":
                        parts_list.append(num)
                        continue
            indexes = find_index_of_num(num, data)
            if indexes[0] - 1 > 0:
                if not data_line[line_index][indexes[0]-1].isdigit() and data_line[line_index][indexes[0]-1] != ".":
                    parts_list.append(num)
                    continue
            if indexes[-1]+1 < len(data_line):
                if not data_line[line_index][indexes[-1]+1].isdigit() and data_line[line_index][indexes[-1]+1] != ".":
                    parts_list.append(num)
                    continue

    sum = 0
    for index, value in enumerate(parts_list):
        parts_list[index] = int(value)
        sum += parts_list[index]
    print(parts_list)
    return sum

def find_index_of_num(num:str, data:str):
    return_list = []
    index = data.find(num)
    while not (index == 0 or not data[index - 1].isalnum()) and \
            (index + len(num) == len(data) or not data[index + len(num)].isalnum()):
        index = data.find(num,index+1)
    for i in range(len(num)):
        return_list.append(index+i)

    return return_list



# def check_num_adjacent_to_symbal()

    # return
with open("input.txt") as f:
    data = f.read()
    print(find_sum_of_parts(data))



def get_neighbours(tuple, ncols, nrows):
    cols = sorted([tuple[i][1] for i in range(1, len(tuple))])
    neighbours = []
    for i in range(tuple[0]-1 , tuple[0]+2):
        for j in range(cols[0]-1, cols[-1] + 2):
            if 0 <= i < nrows and 0 <= j < ncols and (i,j) not in tuple:
                neighbours.append((i,j))
    return neighbours

with open('input.txt') as file:
    input_arr = [list(line) for line in file.read().strip().split('\n')]

nrows = len(input_arr)
ncols = len(input_arr[0])

symbols = []
numbers = {}
for i in range(nrows):
    number = ''
    indices = [i]
    for j in range(ncols):
        if not input_arr[i][j].isdigit() and input_arr[i][j] != '.':
            symbols.append((i,j))
            if number != '':
                numbers[tuple(indices)] = number
                number = ''
                indices = [i]
        elif input_arr[i][j].isdigit():
            number += input_arr[i][j]
            indices.append((i,j))
        elif input_arr[i][j] == '.':
            if number != '':
                numbers[tuple(indices)] = number
                number = ''
                indices = [i]
    if number != '':
        numbers[tuple(indices)] = number


part_sum = 0
part_numbers = []
for key, value in numbers.items():
    neighbours = get_neighbours(key, ncols, nrows)
    if len([indice for indice in neighbours if indice in symbols]) > 0:
        part_sum += int(value)
        part_numbers.append(int(value))

print("Part 1: ", part_sum)
print(part_numbers)
d = "291..217..1..................321......-...................17.....*.......810............411......573.688...273.....*....$.............../..."
print(find_index_of_num("17",d))