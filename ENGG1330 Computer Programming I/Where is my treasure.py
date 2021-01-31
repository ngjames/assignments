
def match(x, y, treasure, map):
    for a in range(len(treasure)-1):
        for b in range(len(treasure)-1):
            if treasure[a][b] != map[x+a][y+b]:
                return False
    return True

def rotate(x):
    return list(zip(*x[::-1]))

found = False
treasure1st = input()
treasure = []
treasure.append(treasure1st)
for x in range(len(treasure1st)-1):
    treasure.append(input())

map1st = input()
map = []
map.append(map1st)
for x in range(len(map1st)-1):
    map.append(input())

for x in range(len(map1st)-len(treasure1st)+1):
    if not found:
        for y in range(len(map1st)-len(treasure1st)+1):
            if match(x, y, treasure, map):
                print(y, x)
                found = True
dir = 0
while dir != 3 and not found:
    treasure = rotate(treasure)
    for x in range(len(map1st)-len(treasure1st)+1):
        if not found:
            for y in range(len(map1st)-len(treasure1st)+1):
                if match(x, y, treasure, map):
                    print(y, x)
                    found = True
    dir += 1