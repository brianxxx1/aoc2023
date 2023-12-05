

def find_location(seed, list):
    seed = int(seed)
    for item in list:
        for i in item:
            if i[1] <= seed <= i[1]+i[-1]-1:
                seed = i[0] + seed - i[1]
                break
    return seed
# part 1
# with open("input.txt") as f:
#     data = f.read()
#     data_split = data.split("\n")
#     data_raw = [item for item in data_split if item != ""]
#
#     seeds = data_raw[0].split(":")[1].split(" ")
#     seeds = [item for item in seeds if item != ""]
#     data = data.split("map:")
#     list = []
#     for item in data[1:]:
#         lst = [i for i in item.split("\n") if i != "" and "to" not in i]
#         for index, element in enumerate(lst):
#             lst[index] = [int(i) for i in element.split()]
#         list.append(lst)
#     min_location = None
#     for seed in seeds:
#         location = find_location(seed, list)
#         if not min_location or location<min_location:
#             min_location = location
#     print(min_location)



# part 2
with open("input.txt") as f:
    data = f.read()
    data_split = data.split("\n")
    data_raw = [item for item in data_split if item != ""]

    seeds = data_raw[0].split(":")[1].split(" ")
    seeds = [item for item in seeds if item != ""]
    data = data.split("map:")
    list = []
    for item in data[1:]:
        lst = [i for i in item.split("\n") if i != "" and "to" not in i]
        for index, element in enumerate(lst):
            lst[index] = [int(i) for i in element.split()]
        list.append(lst)
    new_seeds = []
    min_location = None
    for i in range(len(seeds)):
        if i % 2 == 0:
            print(i)
            for seed in range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])):
                if seed%1000000 == 0:
                    print(seed)
                location = find_location(seed, list)
                if not min_location or location < min_location:
                    min_location = location
    print(min_location)

