def checkwin(x):
    i = len(x)
    j = len(x[0])
    match = ""
    hold = ""
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
    notfounddiag1 = False
    notfounddiag2 = False
    hold = ""
    for y in range(i):
        hold += x[y][y]
        if hold == "X"*i or hold == "O"*i:
            match = hold[0]
    hold = ""
    for y in range(i):
        hold += x[y][i-1-y]
        if hold == "X"*i or hold == "O"*i:
            match = hold[0]
            
    #give back result
    return match

def printboard(x):
    for u in range(len(x)):
        outp = ""
        for z in x[u]:
            s = str(z)
            outp += f"{s:>2}"+" "
        print(outp[:-1:])
###main program
#init board
accumulate = 0
m = ""
times = 0
last = "O"
size = int(input("Size--> "))
b = [["0"]*size for i in range(size)]
for i in range(size):
    for j in range(size):
        b[i][j] = str(accumulate)
        accumulate += 1
#input time!finally :)
#this takes a lot of time arrrrrrrrrr
#btw music is good with programming, makes u relaxed and have a clearer mind
printboard(b)
while m == "" and times < size **2:
    if last == "O":
        inp = int(input("X--> "))
        last = "X"
    elif last == "X":
        inp = int(input("O--> "))
        last = "O"
    b[inp//size][inp%size] = last
    m = checkwin(b)
    printboard(b)
    times += 1
    
result = checkwin(b)
if result == "":
    print("Winner: None")
else:
    print("Winner:", result)
