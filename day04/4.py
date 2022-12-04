f = open("4.txt", "r")
minif = open("4mini.txt", "r")

inputs = f.read().strip().split("\n")
miniinputs = minif.read().strip().split("\n")

#Part 1
def part1(inputs):
    count = 0
    for i in inputs:
        p1, p2 = i.split(",")
        p1min, p1max = int(p1.split("-")[0]), int(p1.split("-")[1])
        p2min, p2max = int(p2.split("-")[0]), int(p2.split("-")[1])
        if (p1min <= p2min and p1max >= p2max) or (p1min >= p2min and p1max <= p2max):
            count += 1
    return count


#Part 2
def part2(inputs):
    count = 0
    for i in inputs:
        p1, p2 = i.split(",")
        p1min, p1max = int(p1.split("-")[0]), int(p1.split("-")[1])
        p2min, p2max = int(p2.split("-")[0]), int(p2.split("-")[1])
        if max(p1min, p2min) <= min(p1max, p2max):
            count += 1
    return count

print("REAL", part1(inputs))
print("MINI", part1(miniinputs))

print("REAL", part2(inputs))
print("MINI", part2(miniinputs))