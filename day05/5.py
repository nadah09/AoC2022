f = open("5.txt", "r")
minif = open("5mini.txt", "r")

inputs = f.read().strip().split("\n\n")
miniinputs = minif.read().strip().split("\n\n")

miniboard = {1: "NZ", 2: "DCM", 3: "P"}
board = {1: "NRJTZBDF", 2: "HJNSR", 3: "QFZGJNRC", 4: "QTRGNVF", 5: "FQTL", 
        6: "NGRBZWCQ", 7: "MHNSLCF", 8: "JTMQND", 9: "SGP"}

#Part 1
def part1(inputs, board):
    inst = inputs[1].split("\n")
    for i in inst:
        _, num, _, p1, _, p2 = i.split(" ")
        p1, p2 = int(p1), int(p2)
        board[p2] = board[p1][:int(num)][::-1] + board[p2]
        board[p1] = board[p1][int(num):]
    
    return "".join(board[i+1][0] for i in range(max(board)))


#Part 2
def part2(inputs, board):
    inst = inputs[1].split("\n")
    for i in inst:
        _, num, _, p1, _, p2 = i.split(" ")
        p1, p2 = int(p1), int(p2)
        board[p2] = board[p1][:int(num)] + board[p2]
        board[p1] = board[p1][int(num):]
    
    return "".join(board[i+1][0] for i in range(max(board)))



print("REAL", part1(inputs, board))
print("MINI", part1(miniinputs, miniboard))

print("REAL", part2(inputs, board))
print("MINI", part2(miniinputs, miniboard))