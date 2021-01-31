dx, dy = input("Position of Queenie: ").split() #d for dummy
qx = int(dx)
qy = int(dy)
arr = []
nPuppies = int(input("Number of puppies: "))
for num in range(1,nPuppies + 1):
    x, y = input("Position of Puppy "+str(num)+": ").split()
    arr.append(int(x))
    arr.append(int(y))
too_far = []
for x in range(nPuppies):
    if (abs(arr[2 * x] - qx) + abs(arr[2*x + 1] - qy) > 10):
        too_far.append(str(x+1))
if len(too_far) == 1:
    print("Puppy", too_far[0], "too far away")
elif len(too_far) == 0:
    print("No puppies too far away")
else:
    output = ""
    for x in too_far:
        output += "Puppy " + x + " and "
    print(output[:-5:], "too far away")