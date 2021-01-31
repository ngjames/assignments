def checkwin(x):
    i = len(x)
    j = len(x[0])
    match = ""
    #check horizontal
    cx = []
    co = []
    for e in range(j):
        cx.append("X")
    for e in range(j):
        co.append("O")
    for y in range(i):
        if x[y] == co or x[y] == cx:
            match = x[y][0]
            
    #check vertical
    for y in range(j):
        acc = ""
        for z in range(i):
            acc+=x[z][y]
        if acc == "X"*i or acc == "O"*i:
            match = acc[0]
            
    #check diagonal
    if (x[1][1] == x[0][0] and x[1][1] == x[2][2]) or (x[1][1] == x[0][2] and x[1][1] == x[2][0]):
        match = x[1][1]
    return match

def printboard(x):
    for u in range(len(x)):
        outp = ""
        for z in x[u]:
            outp += str(z)
        print(outp[::])

accumulate = 0
last = "O"
m = ""
b = [["0","1","2"],["3","4","5"],["6","7","8"]]
printboard(b)
while accumulate < 9 and m == "":
    accumulate += 1
    if last == "O" and m == "":
        i = int(input("X--> "))
        if i < 3:
            b[0][i] = "X"
        elif i < 6:
            b[1][i-3] = "X"
        else:
            b[2][i-6] = "X"
        last = "X"
    elif last == "X" and m =="":
        i = int(input("O--> "))
        if i < 3:
            b[0][i] = "O"
        elif i < 6:
            b[1][i-3] = "O"
        else:
            b[2][i-6] = "O"
        last = "O"
    m = checkwin(b)
    printboard(b)
    
if checkwin(b) == "":
    print("Winner: None")
else:
    print("Winner: " + m)