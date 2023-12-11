def expand(map):
    row_index = 0
    while row_index < len(map):

        if "#" not in map[row_index]:
            map.insert(row_index, ["."]*len(map[row_index]))
            row_index = row_index + 2
            continue
        row_index += 1
    column_index = 0
    while column_index < len(map[0]):
        if "#" not in [map[i][column_index] for i in range(len(map))]:
            for row_index in range(len(map)):
                map[row_index].insert(column_index, ".")
            column_index = column_index + 2
            continue
        column_index += 1
    return map
# with open("input.txt") as f:
#     data = f.read()
#     data = data.split("\n")
#     map = []
#
#     for d in data:
#         map.append(list(d))
#
#     expand(map)
#     index = 1
#     mapping = {}
#     for row_index,row in enumerate(map):
#         for element_index, element in enumerate(row):
#             if element == "#":
#                 mapping[index] = (row_index, element_index)
#                 map[row_index][element_index] = index
#                 index += 1
#
#     sum = 0
#     for key,value in mapping.items():
#         for key2,value2 in mapping.items():
#             if key2 > key:
#                 print(key)
#                 print(key2)
#                 print((abs(value2[0]-value[0])+abs(value2[1]-value[1])))
#                 sum += (abs(value2[0]-value[0])+abs(value2[1]-value[1]))
#     print(sum)


#p2
with open("input.txt") as f:
    data = f.read()
    data = data.split("\n")
    map = []

    for d in data:
        map.append(list(d))
    row_expand_index = []
    column_expand_index = []
    row_index = 0
    while row_index < len(map):
        if "#" not in map[row_index]:
            row_expand_index.append(row_index)
            row_index += 1
            continue
        row_index += 1
    column_index = 0
    while column_index < len(map[0]):
        if "#" not in [map[i][column_index] for i in range(len(map))]:
            column_expand_index.append(column_index)
            column_index += 1
            continue
        column_index += 1
    print(row_expand_index)
    print(column_expand_index)
    index = 1
    mapping = {}
    for row_index, row in enumerate(map):
        for element_index, element in enumerate(row):
            if element == "#":
                mapping[index] = (row_index, element_index)
                map[row_index][element_index] = index
                index += 1
    print(mapping)
    sum = 0
    for key, value in mapping.items():
        for key2, value2 in mapping.items():
            if key2 > key:
                start = min([value[0], value2[0]])
                end = max([value[0], value2[0]])
                count = len([num for num in row_expand_index if start <= num <= end])
                start = min([value[1], value2[1]])
                end = max([value[1], value2[1]])
                count_column = len([num for num in column_expand_index if start <= num <= end])


                sum += (abs(value2[0] - value[0])+count*(1000000-1)) + abs(value2[1] - value[1]) + count_column*(1000000-1)
    print(sum)