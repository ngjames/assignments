def scan3x3(a,b):
    for z in range(3):
        for y in range(3):
            if a+z-1<len(inp) and a+z-1>= 0 and b+y-1 < len(inp) and b+y-1 >= 0:
                if dangerous[a+z-1][b+y-1] == "1":
                    return False
    return True

def scan5x5(a,b):
    for z in range(5):
        for y in range(5):
            if a+z-2<len(inp) and a+z-2>= 0 and b+y-2 < len(inp) and b+y-2 >= 0:
                if dangerous[a+z-2][b+y-2] == "1":
                    return False
    return True

dangerous = []
inp = list(input())
dangerous.append(inp)
for x in range(len(inp)-1):
    dangerous.append(list(input()))
safety = [["2" for x in range(len(inp))] for j in range(len(inp))]

for a in range(len(inp)):
    for b in range(len(inp)):
        if dangerous[a][b] == "1":
            safety[a][b] = "#"
        
for a in range(len(inp)):
    for b in range(len(inp)):
        if not safety[a][b] == "#":
            if scan3x3(a, b):
                if scan5x5(a, b):
                    safety[a][b] = "2"
                else:
                    safety[a][b] = "1"
            else:
                safety[a][b] = "0"
for x in safety:
    a = ""
    for y in x:
        a+=y
    print(a)