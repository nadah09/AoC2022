f = open("10.txt", "r")
minif = open("10mini.txt", "r")

from collections import defaultdict

inputs = f.read().strip().split("\n")
miniinputs = minif.read().strip().split("\n")

#Part 1
def part1(inputs):
    cycles = 0
    x = 1
    signals = 0
    s = [20, 60, 100, 140, 180, 220]

    for i in inputs:
        if i == "noop":
            cycles += 1
            if cycles in s:
                signals += x*cycles
        else:
            inst, num = i.split(" ")
            num = int(num)
            cycles += 1
            if cycles in s:
                signals += x*cycles
            cycles += 1
            if cycles in s:
                signals += x*cycles
            x += num
    return signals

#Part 2
def update(grid, x, cycles):
    cycles += 1
    if abs(x-(cycles-1)%40) <= 1:
        grid[(cycles-1)//40][(cycles-1)%40] = "#"
    return grid, cycles

def part2(inputs):
    grid = [[" " for i in range(40)] for j in range(6)]
    cycles = 0
    x = 1
    signals = 0
    for i in inputs:
        if i == "noop":
            grid, cycles = update(grid, x, cycles)
        else:
            num = int(i[5:])
            grid, cycles = update(grid, x, cycles)
            grid, cycles = update(grid, x, cycles)
            x += num
    for row in grid:
        print("".join(row))


print("REAL", part1(inputs))
print("MINI", part1(miniinputs))

print("REAL", part2(inputs))
print("MINI", part2(miniinputs))