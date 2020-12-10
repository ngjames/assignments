x = [int(x) for x in input("Numbers: ").split()]
ind = []
count = 0
for num in x:
    ind.append([])
    for i in range(1,num):
        if num % i == 0:
            ind[count].append(i)
    count+=1
prp = True
for i in range(len(ind)-1):
    if ind[i+1] != [] and ind[i] != []:
        if set(ind[i]) & set(ind[i+1]) != {1}:
            prp = False
if prp:
    print("prp")
else:
    loop = 0
    while ind[loop] == []:
        loop += 1
    comp = set(ind[loop])
    for i in range(loop, len(ind)-2):
        comp = comp & set(ind[i+2])
    if comp == {1}:
        print("mrp")
    else:
        print("~")