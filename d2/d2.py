## Advent of Code 2023, Day 2
import re


# Part 1 ======================================================================================================================

def is_the_game_possible(game_str: str) -> int:
    game_result = game_str.split(":",1)[1].split(";")
    for subset in game_result:
        single_game = subset.split(",")
        for color in single_game:
            if "red" in color:
                red_num = int(re.findall(r'\d+', color)[0])
                if red_num > 12:
                    return 0
            if "green" in color:
                green_num = int(re.findall(r'\d+', color)[0])
                if green_num > 13:
                    return 0
            if "blue" in color:
                blue_num = int(re.findall(r'\d+', color)[0])
                if blue_num > 14:
                    return 0
    game_id = int(re.findall(r'\d+', game_str.split(":", 1)[0])[0])
    return game_id

def find_minimum_cubes(game_str: str) -> int:
    game_result = game_str.split(":", 1)[1].split(";")
    minimum_cubes = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for subset in game_result:
        single_game = subset.split(",")
        for color in single_game:
            if "red" in color:
                red_num = int(re.findall(r'\d+', color)[0])
                cur_min_red = minimum_cubes["red"]
                if red_num > cur_min_red:
                    minimum_cubes["red"] = red_num
            if "green" in color:
                green_num = int(re.findall(r'\d+', color)[0])
                cur_min_green = minimum_cubes["green"]
                if green_num > cur_min_green:
                    minimum_cubes["green"] = green_num
            if "blue" in color:
                blue_num = int(re.findall(r'\d+', color)[0])
                cur_min_blue = minimum_cubes["blue"]
                if blue_num > cur_min_blue:
                    minimum_cubes["blue"] = blue_num

    return minimum_cubes["red"] * minimum_cubes["green"] * minimum_cubes["blue"]


with open("input.txt") as f:
    data = f.read().splitlines()
    sum = 0
    for game in data:
        sum += find_minimum_cubes(game)
    print(sum)

