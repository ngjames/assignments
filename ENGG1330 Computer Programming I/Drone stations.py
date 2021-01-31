a, b = input().split()
station = [[0,0]]
if int(a)> 0:
    for x in range(int(a)):
        t, g = input().split()
        station.append([int(t), int(g)])
v, r = input().split()
station[0][0], station[0][1] = int(v), int(r)
v, r = input().split()
station.append([int(v), int(r)])
edge = {}
for x in range(len(station)):
    edge[x] = []
    for y in range(len(station)):
        if x!=y:
            if ((station[x][0]-station[y][0])**2 + (station[x][1]-station[y][1])**2)**0.5 <= int(b):
                edge[x].append(y)

src = 0
des = len(station)-1
q = []
visited = {}
previous = {}
q.append(int(src))
for x in range(len(station)):
    visited[x] = False
visited[src] = True
#search
while (visited[len(station)-1] == False and len(q) != 0):
    current = q.pop(0)
    for n in edge[current]:
        if visited[n] == False:
            q.append(n)
            visited[n] = True
            previous[n] = current
result = int(des)
pathh = []
err = False
while result != src:
    pathh.append(result)
    try:
        result = previous[result]
    except:
        err = True
        break
if err:
    print("n")
else:
    print("y")
