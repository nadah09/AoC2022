f = open("11.txt", "r")
minif = open("11mini.txt", "r")

from collections import defaultdict

inputs = f.read().strip().split("\n\n")
miniinputs = minif.read().strip().split("\n\n")

def process(inputs):
    monkeys = defaultdict(int)
    ops = defaultdict(list)
    tests = defaultdict(int)
    true = defaultdict(int)
    false = defaultdict(int)

    for m in inputs:
        lines = m.split("\n")
        monkey = int(lines[0].strip().split(" ")[1].strip(":")[0])
        monkeys[monkey] = [int(i) for i in lines[1].split(": ")[1].split(", ")]
        ops[monkey] = lines[2].split(": ")[1].split("= ")[1].split(" ")
        tests[monkey] = int(lines[3].split(" ")[-1])
        true[monkey] = int(lines[4].split(" ")[-1])
        false[monkey] = int(lines[5].split(" ")[-1])

    mod = 1
    for i in tests.values():
        mod *= i

    return monkeys, ops, tests, true, false, mod


def simulate(inputs, rounds):
    monkeys, ops, tests, true, false, mod = process(inputs)
    count = defaultdict(int)

    for i in range(rounds):
        for m in sorted(monkeys):
            worry = monkeys[m]
            op = ops[m]
            monkeys[m] = []
            test = tests[m]
            t_m = true[m]
            f_m = false[m]
            for w in worry:
                count[m] += 1
                try:
                    val1 = int(op[0])
                except:
                    val1 = w
                try:
                    val2 = int(op[2])
                except:
                    val2 = w
                if op[1] == "+":
                    new = val1 + val2
                elif op[1] == "*":
                    new = val1 * val2
                new %= mod
                if rounds == 20:
                    new = new//3
                if new%test == 0:
                    monkeys[t_m].append(new)
                else:
                    monkeys[f_m].append(new)

    counts = sorted(count.values())
    return counts[-1]*counts[-2]

def part1(inputs):
    return simulate(inputs, 20)

#Part 2
def part2(inputs):
    return simulate(inputs, 10000)

print("REAL", part1(inputs))
print("MINI", part1(miniinputs))

print("REAL", part2(inputs))
print("MINI", part2(miniinputs))