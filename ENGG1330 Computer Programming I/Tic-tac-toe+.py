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
            acc+=str(x[z][y])
        if acc == "X"*i or acc == "O"*i:
            match = acc[0]
            
    #check diagonal
    if (x[1][1] == x[0][0] and x[1][1] == x[2][2]) or (x[1][1] == x[0][2] and x[1][1] == x[2][0]):
        match = x[1][1]
    #give back result
    return match

def printboard(x):
    for u in range(len(x)):
        outp = ""
        for z in x[u]:
            outp += str(z)
        print(outp[::])

#initialize variable
b = [["0"]*3 for i in range(3)]
xcor = []
ycor = []
accumulate = 0
last = "O"

#main
for i in range(3):
    for j in range(3):
        b[i][j] = accumulate
        accumulate += 1
r = input("Replay: ").split("->")

for x in r:
    xcor.append(int(x[1]))
    ycor.append(int(x[3]))
printboard(b)
for x in range(len(r)):
    if last == "O":
        print("X-->", xcor[x]*3+ycor[x])
        last = "X"
        b[xcor[x]][ycor[x]] = "X"
    else:
        print("O-->", xcor[x]*3+ycor[x])
        last = "O"
        b[xcor[x]][ycor[x]] = "O"
    printboard(b)
result = checkwin(b)
if result == "":
    print("Winner: None")
else:
    print("Winner:", result)