import copy

def boarddead(x):
    if x[1][1] == "X":
        if x[0][2] == "X" and x[2][0] == "X":
            return True
        if x[0][0] == "X" and x[2][2] == "X":
            return True
    for a in range(3):
        hold = ""
        for b in range(3):
            hold += str(x[a][b])
        if hold == "XXX":
            return True
    for a in range(3):
        hold = ""
        for b in range(3):
            hold += str(x[b][a])
        if hold == "XXX":
            return True
    return False
    

def translator(x):
    if x == 0:
        return "A"
    if x == 1:
        return "B"
    if x == 2:
        return "C"
    if x == "A":
        return 0
    if x == "B":
        return 1
    if x == "C":
        return 2
    return "ERR"

def printboard(DeadBoard):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for x in {0,1,2} - DeadBoard:
        line1 += translator(x)+"      "
        line2 += str(board[x][0][0])+ " "+ str(board[x][0][1])+ " "+ str(board[x][0][2]) + "  " 
        line3 += str(board[x][1][0])+ " "+ str(board[x][1][1])+ " "+ str(board[x][1][2]) + "  " 
        line4 += str(board[x][2][0])+ " "+ str(board[x][2][1])+ " "+ str(board[x][2][2]) + "  " 
    print(line1[:-6:])
    print(line2[:-2:])
    print(line3[:-2:])
    print(line4[:-2:])
    z = copy.deepcopy(avaliable_move)
    
def inputsanitycheck(x, DeadBoard):
    if len(x) != 2:
        return False
    if translator(x[0]) not in ({0,1,2} - DeadBoard):
        return False
    try:
        int(x[1])
    except:
        return False
    if int(x[1]) not in range(9):
        return False
    if board[translator(inp[0])][(int(inp[1]))//3][(int(inp[1])+1)%3 -1] == "X":
        return False
    return True
    
def rotate(rota):
    return list(zip(*rota[::-1]))

def fingerprintcheck(b):
    x = 0
    while x < 4:
        if b in fpa:
            return "a"
        if b in fpb:
            return "b"
        if b in fpc:
            return "c"
        if b in fpc2:
            return "cc"
        if b in fpd:
            return "d"
        if b in fpab:
            return "ab"
        if b in fpad:
            return "ad"
        if b in fp1:
            return ""
        b = rotate(b)
        x += 1

def lose(y):
    if boarddead(y):
        return True
    return False
        
def aimove():
    combinedfp = ""
    for x in avaliable_move:
        y = copy.deepcopy(stripped)
        y[translator(x[0])][(int(x[1]))//3][(int(x[1])+1)%3 -1] = "X"
        for z in {0,1,2} - deadboard:
            f = fingerprintcheck(y[z])
            try:
                combinedfp += f
            except:
                er = 0
        a = list(combinedfp)
        a.sort()
        if (a in winning_fp) and (not lose(y[translator(x[0])])):
            return x
        combinedfp = ""
    return avaliable_move[0]
    
        

fpa  = [[["X","0","0"],["0","0","0"],["0","0","X"]],[["0","X","0"],["X","0","0"],["0","0","0"]],[["0","X","0"],["0","0","0"],["0","X","0"]],[["X","X","0"],["0","0","0"],["X","0","0"]],[["X","0","X"],["0","X","0"],["0","0","0"]],[["X","0","X"],["0","0","0"],["0","X","0"]],[["X","0","0"],["0","X","X"],["0","0","0"]],[["X","X","0"],["X","X","0"],["0","0","0"]],[["X","X","0"],["X","0","X"],["0","0","0"]],[["X","X","0"],["X","0","0"],["0","0","X"]],[["X","0","X"],["0","0","0"],["X","0","X"]],[["0","X","0"],["X","0","X"],["0","X","0"]],[["X","X","0"],["0","0","0"],["0","X","X"]],[["X","X","0"],["0","X","X"],["X","0","0"]],[["X","X","0"],["0","0","X"],["X","X","0"]],[["X","X","0"],["0","0","X"],["X","0","X"]],[["X","X","0"],["X","0","X"],["0","X","X"]]]
fpb  = [[["X","0","X"],["0","0","0"],["0","0","0"]],[["X","0","0"],["0","X","0"],["0","0","0"]],[["X","0","0"],["0","0","X"],["0","0","0"]],[["0","X","0"],["0","X","0"],["0","0","0"]],[["X","X","0"],["X","0","0"],["0","0","0"]],[["0","X","0"],["X","0","X"],["0","0","0"]],[["X","X","0"],["0","X","X"],["0","0","0"]],[["X","X","0"],["0","X","0"],["X","0","0"]],[["X","X","0"],["0","0","X"],["X","0","0"]],[["0","0","0"],["X","X","0"],["X","X","0"]],[["X","0","X"],["0","X","0"],["0","X","0"]],[["X","0","0"],["0","X","X"],["0","X","0"]],[["X","X","0"],["0","0","0"],["X","0","X"]],[["X","X","0"],["X","0","X"],["0","X","0"]],[["X","X","0"],["X","0","X"],["0","0","X"]]]
fpc  = [[["0","0","0"],["0","0","0"],["0","0","0"]]]
fpc2 = [[["0","0","0"],["0","X","0"],["0","0","0"]]]
fpd  = [[["X","X","0"],["0","0","X"],["0","0","0"]],[["X","X","0"],["0","0","0"],["0","X","0"]],[["X","X","0"],["0","0","0"],["0","0","X"]]]
fpab = [[["X","X","0"],["0","X","0"],["0","0","0"]],[["X","0","X"],["0","0","0"],["X","0","0"]],[["0","X","0"],["X","X","0"],["0","0","0"]],[["X","X","0"],["0","0","X"],["0","X","0"]],[["X","X","0"],["0","0","X"],["0","0","X"]]]
fpad = [[["X","X","0"],["0","0","0"],["0","0","0"]]]
fp1  = [[["X","0","0"],["0","0","0"],["0","0","0"]],[["0","X","0"],["0","0","0"],["0","0","0"]],[["X","0","0"],["0","0","X"],["0","X","0"]],[["X","X","0"],["0","X","0"],["0","0","X"]]]
avaliable_move = ["A0", "A1", "A2","A3", "A4", "A5", "A6", "A7", "A8", "B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C0", "C1", "C2", "C3","C4", "C5", "C6", "C7", "C8"]
winning_fp = [["c", "c"], ["a"], ["b", "b"], ["b", "c"]]

board = [[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]]]
deadboard = set()
stripped = [[["0","0","0"],["0","0","0"],["0","0","0"]],[["0","0","0"],["0","0","0"],["0","0","0"]],[["0","0","0"],["0","0","0"],["0","0","0"]]]
who = []
lastplayer = 2
noWin = True
while noWin:
    printboard(deadboard)
    if lastplayer == 2:
        inp = aimove()
        print ("Player 1:", inp)
        avaliable_move.remove(inp)
        board[translator(inp[0])][(int(inp[1]))//3][(int(inp[1])+1)%3 -1] = "X"
        stripped[translator(inp[0])][(int(inp[1]))//3][(int(inp[1])+1)%3 -1] = "X"
        if boarddead(board[translator(inp[0])]):
            deadboard.add(translator(inp[0]))
            d = copy.deepcopy(avaliable_move)
            for e in d:
                if e[0] == inp[0]:
                    avaliable_move.remove(e)
                    
            who.append(1)
            if deadboard == {0,1,2}:
                noWin = False
        lastplayer = 1
    elif lastplayer == 1:
        inp = input("Player 2: ")
        while not inputsanitycheck(inp, deadboard):
            print("Invalid move, please input again")
            inp = input("Player 2: ")
        avaliable_move.remove(inp)
        board[translator(inp[0])][(int(inp[1]))//3][(int(inp[1])+1)%3 -1] = "X"
        stripped[translator(inp[0])][(int(inp[1]))//3][(int(inp[1])+1)%3 -1] = "X"
        if boarddead(board[translator(inp[0])]):
            deadboard.add(translator(inp[0]))
            d = copy.deepcopy(avaliable_move)
            for e in d:
                if e[0] == inp[0]:
                    avaliable_move.remove(e)
            who.append(2)
            if deadboard == {0,1,2}:
                noWin = False
        lastplayer = 2
        
a = 0
b = 0
for x in who:
    if x == 1:
        a += 1
    if x == 2:
        b += 1
if a>b:
    print("Player 2 wins game")
else:
    print("Player 1 wins game")