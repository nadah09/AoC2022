f = open("6.txt", "r")
minif = open("6mini.txt", "r")

inputs = f.read().strip().split("\n")[0]
miniinputs = minif.read().strip().split("\n")[0]

#Part 1
def part1(inputs):
    marker = [i+4 for i in range(len(inputs)-3) if len(set(inputs[i:i+4])) == 4]
    return min(marker)

#Part 2
def part2(inputs):
    marker = [i+14 for i in range(len(inputs)-13) if len(set(inputs[i:i+14])) == 14]
    return min(marker)


print("REAL", part1(inputs))
print("MINI", part1(miniinputs))

print("REAL", part2(inputs))
print("MINI", part2(miniinputs))