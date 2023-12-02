## Advent of Code 2023, Day 1

# Part 1 ======================================================================================================================
def find_first_digit_from_left_and_right(word: str) -> int:
    n = len(word)
    left_digit = None
    right_digit = None
    for i in range(n):
        if word[i].isdigit():
            left_digit = word[i]
            break
    for i in range(n - 1, -1, -1):
        if word[i].isdigit():
            right_digit = word[i]
            break
    return int(left_digit+right_digit)


with open("input.txt") as f:
    data = f.read().splitlines()
    sum = 0
    for word in data:
        num = find_first_digit_from_left_and_right(word)
        sum += num
    print(sum)



# Part 2 ======================================================================================================================
def find_first_digit_from_left_and_right_with_spelled_num(word: str) -> int:
    n = len(word)
    left_digit = None
    right_digit = None
    num_names = ['zero','one','two','three','four','five','six','seven','eight','nine']
    outer_break = False
    for i in range(n):
        if word[i].isdigit():
            left_digit = word[i]
            break
        else:
            for j in num_names:
                if word[i: i+len(j)] == j:
                    left_digit = str(num_names.index(j))
                    outer_break = True
                    break
            if outer_break:
                break


    outer_break = False
    for i in range(n - 1, -1, -1):
        if word[i].isdigit():
            right_digit = word[i]
            break
        else:
            for j in num_names:
                if word[i-len(j)+1: i+1] == j:
                    right_digit = str(num_names.index(j))
                    outer_break = True
                    break
            if outer_break:
                break
    return int(left_digit+right_digit)

with open("input.txt") as f:
    data = f.read().splitlines()
    sum = 0
    for word in data:
        num = find_first_digit_from_left_and_right_with_spelled_num(word)
        sum += num
    print(sum)
