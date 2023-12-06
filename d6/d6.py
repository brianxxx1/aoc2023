
def find_num_of_ways_to_win(time ,distance):
    num_of_ways_to_win = 0
    for i in range(time):
        velocity = i
        distance_traveled = (time - i) * velocity
        if distance_traveled > distance:
            num_of_ways_to_win += 1
    return num_of_ways_to_win

    # part 1
with open("input.txt") as f:
    data = f.read()
    data_split = data.split("\n")
    data_raw = [item.split(" ") for item in data_split if item != ""]
    time = [ int(item) for item in data_raw[0] if item.isdigit()]
    distance = [ int(item) for item in data_raw[1] if item.isdigit()]
    result = 1
    # for index, value in enumerate(time):
    #     result = result * find_num_of_ways_to_win(value, distance[index])
    # print(result)
    time_to_use = ""
    for t in time:
        time_to_use+=str(t)
    distance_to_use = ""
    for d in distance:
        distance_to_use += str(d)
    print(find_num_of_ways_to_win(int(time_to_use), int(distance_to_use)))

