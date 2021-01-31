length = int(input("Length of riverfront: "))
ans = set(range(0, length))
animals = int(input("Number of animals: "))
for x in range(animals):
    start, stop = input("Animal " + str(x + 1)+": ").split()
    ans = ans - set(range(int(start), int(stop) + 1))
ans = sorted(ans)
max_cons = 1
cons = 1
conv = list(ans)
for i in range(len(conv)-1):
    if conv[i + 1] - conv[i] == 1:
        cons += 1
        if cons > max_cons:
            max_cons = cons
    else:
        cons = 1
if ans == []:
    print(0)
elif max_cons > length:
    print(length)
else:
    print(max_cons)