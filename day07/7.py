f = open("7.txt", "r")
minif = open("7mini.txt", "r")

from collections import defaultdict

inputs = f.read().strip().split("\n")
miniinputs = minif.read().strip().split("\n")

#Part 1
def part1(inputs):
  d = []
  sizes = defaultdict(int)
  for inst in inputs:
    inst = inst.split(" ")
    if inst[1] == "cd":
      if inst[2] == "..":
        d.pop()
      else:
        d.append(inst[2] + "/")
    elif inst[0] != "$" and inst[0] != "dir":
      size = int(inst[0])
      for i in range(len(d)):
        sizes["".join(d[:i+1])] += size
  return sum([sizes[d] for d in sizes if sizes[d]<=100000])

#Part 2
def part2(inputs):
  d = []
  sizes = defaultdict(int)
  for inst in inputs:
    inst = inst.split(" ")
    if inst[1] == "cd":
      if inst[2] == "..":
        d.pop()
      else:
        d.append(inst[2] + "/")
    elif inst[0] != "$" and inst[0] != "dir":
      size = int(inst[0])
      for i in range(len(d)):
        sizes["".join(d[:i+1])] += size

  unused_space = 70000000 - sizes["//"]
  space_needed = 30000000 - unused_space

  poss = [sizes[d] for d in sizes if sizes[d] >= space_needed]
  return min(poss)


print("REAL", part1(inputs))
print("MINI", part1(miniinputs))

print("REAL", part2(inputs))
print("MINI", part2(miniinputs))