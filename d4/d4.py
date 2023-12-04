## Advent of Code 2023, Day 2


# Part 1 ======================================================================================================================

def find_point_from_card(card:str):
    card = card.split(":")[1]
    win_nums = [item for item in card.split("|")[0].split(" ") if item.isdigit()]
    nums = [item for item in card.split("|")[1].split(" ") if item.isdigit()]
    count = 0
    for win_num in win_nums:
        for num in nums:
            if win_num == num:
                count += 1
    return count


# Part 2 ======================================================================================================================
with open("input.txt") as f:
    data = f.read().splitlines()
    sum = 1
    map = {}
    for index, card in enumerate(data):
        print(index)
        count = find_point_from_card(card)
        sum += count
        for c in range(count):
            if index + 2 + c in map:
                map[index + 2 + c] += 1
            else:
                map[index + 2 + c] = 1
        try:
            for c in range(map[index+1]):
                count = find_point_from_card(card)
                sum += count
                for c in range(count):
                    if index + 2 + c in map:
                        map[index + 2 + c] += 1
                    else:
                        map[index + 2 + c] = 1
        except KeyError:
            pass
    sum = 0
    for key in map:
        sum+=map[key]
    sum += len(data)
    print(sum)