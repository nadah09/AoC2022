f = open("1.txt", "r")
minif = open("1mini.txt", "r")

inputs = f.read().strip().split("\n\n")
miniinputs = minif.read().strip().split("\n\n")

inputs = [[int(i) for i in j.split("\n")] for j in inputs]
miniinputs = [[int(i) for i in j.split("\n")] for j in miniinputs]

#Part 1
def part1(inputs):
	return max([sum(i) for i in inputs])

#Part 2
def part2(inputs):
	scores = [sum(i) for i in inputs]
	return sum(sorted(scores)[-3:])

print(part1(miniinputs))
print(part1(inputs))

print(part2(miniinputs))
print(part2(inputs))