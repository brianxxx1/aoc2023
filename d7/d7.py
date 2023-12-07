

def evaluate_hand_without_j(hand):
    st = {}
    for card in hand:
        if card in st:
            st[card] += 1
        else:
            st[card] = 1
    values = []
    for key, value in st.items():
        values.append(value)
    values.sort()
    max = values[-1]
    if max == 5:
        return 5
    if max == 4:
        return 4
    if max == 3:
        for i in values:
            if i == 2:
                return 3
        return 2
    if max == 2:
        for i in values[:-1]:
            if i == 2:
                return 1
        return 0
    return -1

def evaluate_hand_with_j(hand):
    st = {}
    num_of_j = 0
    for card in hand:
        if card in st:
            st[card] += 1
        elif card == "J":
            num_of_j += 1
        else:
            st[card] = 1
    values = []
    for key, value in st.items():
        values.append(value)
    values.sort()

    try:
        max = values[-1]
    except IndexError:
        return -2
    max = max + num_of_j
    if num_of_j != 0:
        values =values[:-1]
    if max == 5:
        return 5
    if max == 4:
        return 4
    if max == 3:
        for i in values:
            if i == 2:
                return 3
        return 2
    if max == 2:
        for i in values[:-1]:
            if i == 2:
                return 1
        return 0
    return -1

def evaluate_hand(hand):
    return max(evaluate_hand_with_j(hand), evaluate_hand_without_j(hand))

def compare_hands(hands_1, hands_2):
    mapping = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,"2": 2}
    if hands_1[1] > hands_2[1]:
        return True

    if hands_1[1] == hands_2[1]:
        for index in range(len(hands_1[0])):
            if mapping[hands_1[0][index]] > mapping[hands_2[0][index]]:
                return True
            if mapping[hands_1[0][index]] < mapping[hands_2[0][index]]:
                return False
            continue
    return False

# part 2
with open("input.txt") as f:
    data = f.read()
    data_split = data.split("\n")
    hands = []
    bids = []
    for i in data_split:
        hands.append(i.split(" ")[0])
        bids.append(int(i.split(" ")[1]))
    hands_sorted = []
    for index,i in enumerate(hands):
        strength = (i,evaluate_hand(i),bids[index])
        if len(hands_sorted) == 0:
            hands_sorted.append(strength)
            continue
        for index, element in enumerate(hands_sorted):
            if compare_hands(strength, element):
                if index == len(hands_sorted)-1:
                    hands_sorted.append(strength)
                    break
                continue
            hands_sorted.insert(index, strength)
            break

    sum = 0
    for index, hands in enumerate(hands_sorted):
        sum += (index+1)*hands[2]

    for i in hands_sorted:
        print(i[0])
    print(hands_sorted)
    print(sum)

