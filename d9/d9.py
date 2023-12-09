#p2
with open("input.txt") as f:
    data = f.read()
    values = data.split("\n")
    value_list = []
    for value in values:
        value_list.append(value.split(" "))
    for value in value_list:
        for index in range(len(value)):
            value[index] = int(value[index])
    sum = 0
    for value in value_list:
        sequences = []
        diff = value
        sequences.append(diff)
        while not all(x==0 for x in diff):
            diff = [ diff[i] - diff[i-1] for i in range(1,len(diff))]
            sequences.append(diff)
        diff = 0
        for i in reversed(sequences[:-1]):
            diff = i[0] - diff
        sum += diff
    print(sum)