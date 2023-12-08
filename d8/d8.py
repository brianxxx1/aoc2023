
def find_path(start:str) -> int:
    steps = 0
    loc = start
    index = 0
    while not loc.endswith("Z"):
        steps += 1
        next_loc = map.get(loc)[instruction_list[index]]
        if next_loc.endswith("Z"):
            break
        else:
            loc = next_loc
        if index == len(instruction_list) - 1:
            index = 0
        else:
            index += 1
    return steps

# part 1
# with open("input.txt") as f:
#     data = f.read()
#     instruction = data.split("\n")[0]
#     map = data.split("\n")[2:]
#     instruction_list = []
#     for c in instruction:
#         if c == "L":
#             instruction_list.append(0)
#         elif c == "R":
#             instruction_list.append(1)
#
#     starts = []
#     destinations = []
#     for m in map:
#         starts.append(m.split("=")[0].strip())
#         destinations.append(m.split("=")[1].strip(" ()").replace(" ","").split(","))
#     map = {}
#     for index, d in enumerate(starts):
#         map[d] = (destinations[index][0], destinations[index][1])
#
#     steps = 0
#     loc = "AAA"
#     index = 0
#     while loc != "ZZZ":
#         steps += 1
#         next_loc = map.get(loc)[instruction_list[index]]
#         if next_loc == "ZZZ":
#             break
#         else:
#             loc = next_loc
#         if index == len(instruction_list) - 1:
#             index = 0
#         else:
#             index += 1


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the Least Common Multiple of a and b."""
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    """Calculate the LCM of a list of numbers."""
    lcm_result = numbers[0]
    for number in numbers[1:]:
        lcm_result = lcm(lcm_result, number)
    return lcm_result



with open("input.txt") as f:
    data = f.read()
    instruction = data.split("\n")[0]
    map = data.split("\n")[2:]
    instruction_list = []
    for c in instruction:
        if c == "L":
            instruction_list.append(0)
        elif c == "R":
            instruction_list.append(1)

    starts = []
    destinations = []
    for m in map:
        starts.append(m.split("=")[0].strip())
        destinations.append(m.split("=")[1].strip(" ()").replace(" ","").split(","))
    map = {}
    for index, d in enumerate(starts):
        map[d] = (destinations[index][0], destinations[index][1])
    lst = []
    for k, v in map.items():
        if k.endswith("A"):
            lst.append(find_path(k))
    print(lcm_of_list(lst))






