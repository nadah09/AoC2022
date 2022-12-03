f = open("2.txt", "r")
minif = open("2mini.txt", "r")

inputs = f.read().strip().split("\n")
miniinputs = minif.read().strip().split("\n")

#Part 1
def part1(inputs):
    p1 = "ABC"
    p2 = "XYZ"
    score = 0

    for i in inputs:
        o, m = i.split(" ")
        result = (p2.index(m)-p1.index(o)+1)%3
        score += result*3+(p2.index(m)+1)
    return score

#Part 2
def part2(inputs):
    p1 = "ABC"
    p2 = "XYZ"
    score = 0

    for i in inputs:
        o, result = i.split(" ")
        m = (p2.index(result)+p1.index(o)-1)%3
        score += p2.index(result)*3+(m+1)
    return score

print(part1(miniinputs))
print(part1(inputs))

print(part2(miniinputs))
print(part2(inputs))