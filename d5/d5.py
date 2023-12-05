from multiprocessing import Pool


def find_location(seed, list):
    seed = int(seed)
    for item in list:
        for i in item:
            if i[1] <= seed <= i[1]+i[-1]-1:
                seed = i[0] + seed - i[1]
                break
    return seed

def processing_seed_range(start,stop,mappings):
    min_location = None
    for seed in range(start, stop):
        if seed %1000000 == 0:
            print(seed)
        location = find_location(seed, mappings)
        if min_location is None or location < min_location:
            min_location = location
    return min_location

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
if __name__ == '__main__':
    with Pool() as pool:
        args = [(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]), list) for i in range(len(seeds)) if i % 2 == 0]
        results = pool.starmap(processing_seed_range, args)
        min_location = min(results)
        print(min_location)

