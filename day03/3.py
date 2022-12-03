f = open("3.txt", "r")
minif = open("3mini.txt", "r")

inputs = f.read().strip().split("\n")
miniinputs = minif.read().strip().split("\n")

#Part 1
def part1(inputs):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0
    for i in inputs:
        front = set(i[:int(len(i)/2)])
        back = set(i[int(len(i)/2):])
        common = list(front.intersection(back))[0]
        score += letters.index(common)+1
    return score


#Part 2
def part2(inputs):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0
    for i in range(0, len(inputs), 3):
        one = set(inputs[i])
        two = set(inputs[i+1])
        three = set(inputs[i+2])
        common = list(one.intersection(two).intersection(three))[0]
        score += letters.index(common)+1
    return score


print(part1(miniinputs))
print(part1(inputs))

print(part2(miniinputs))
print(part2(inputs))