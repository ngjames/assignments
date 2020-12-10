def boarddead(x):
    if (x[0][0] == x[1][1] and x[2][2] == x[1][1]) or (x[0][2] == x[1][1] and x[2][0] == x[1][1]):
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
    

board = [[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]],[[0,1,2],[3,4,5],[6,7,8]]]
deadboard = set()
who = []
lastplayer = 2
noWin = True
while noWin:
    printboard(deadboard)
    if lastplayer == 2:
        inp = input("Player 1: ")
        while not inputsanitycheck(inp, deadboard):
            print("Invalid move, please input again")
            inp = input("Player 1: ")
        board[translator(inp[0])][(int(inp[1]))//3][(int(inp[1])+1)%3 -1] = "X"
        if boarddead(board[translator(inp[0])]):
            deadboard.add(translator(inp[0]))
            who.append(1)
            if deadboard == {0,1,2}:
                noWin = False
        lastplayer = 1
    elif lastplayer == 1:
        inp = input("Player 2: ")
        while not inputsanitycheck(inp, deadboard):
            print("Invalid move, please input again")
            inp = input("Player 2: ")
        board[translator(inp[0])][(int(inp[1]))//3][(int(inp[1])+1)%3 -1] = "X"
        if boarddead(board[translator(inp[0])]):
            deadboard.add(translator(inp[0]))
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