node={} #Global variable with key as node ID (an integer), value as name of the node.
edge={} #Global variable with key as the node ID (an integer), value as a set of neighbor node ID(s) 
def InsertNode(id,name):
    global node
    global edge
    if int(id) in node:
        print("ID exists.")
    else:
        node[int(id)] = name
        edge[int(id)] = set()
    return
def InsertEdge(id1,id2):
    global node
    global edge
    if int(id1) in node.keys() and int(id2) in node.keys():
        if int(id2) in edge[int(id1)]:
            print("Edge exists.")
        else:
            edge[int(id1)].append(int(id2))
    else:
        print("No such node.")
    return
def CommonNeighbor(id1,id2):
    global node
    global edge
    if int(id1) in node.keys() and int(id2) in node.keys():
        x = edge[int(id1)] & edge[int(id2)]
        if x != set():
            for i in x:
                print(i, node[i])
        else:
            print("No common neighbor.")
    else:
        print("No such node.")
    return
def ShortestPath(src,des):
    global node
    global edge
    #init
    q = []
    visited = {}
    previous = {}
    q.append(int(src))
    for x in node.keys():
        visited[x] = False
    visited[int(src)] = True
    #search
    while (visited[des] == False and len(q) != 0):
        current = q.pop(0)
        for n in edge[current]:
            if visited[n] == False:
                q.append(n)
                visited[n] = True
                previous[n] = current
    result = int(des)
    pathh = []
    err = False
    while result != int(src):
        pathh.append(result)
        try:
            result = previous[result]
        except:
            err = True
            break
    if err:
        print("No path found.")
    else:
        print(src, node[int(src)])
        for x in range(len(pathh)):
            print(pathh[len(pathh)-1-x], node[pathh[len(pathh)-1-x]])
    return
def main():
    command=input().split()
    while(command[0]!="END"):
        if (command[0]=="InsertNode"):
            InsertNode(int(command[1]),command[2])
        elif (command[0]=="InsertEdge"):
            InsertEdge(int(command[1]),int(command[2]))
        elif (command[0]=="CommonNeighbor"):
            CommonNeighbor(int(command[1]),int(command[2]))
        elif (command[0]=="ShortestPath"):
            ShortestPath(int(command[1]),int(command[2]))
        command=input().split()
    return
main()