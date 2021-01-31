user = int(input("Number of users: "))
output = ""
for num in range(1, user +1):
    dx, dy = input("Position of User "+ str(num)+ ": ").split()
    qx = int(dx)
    qy = int(dy)
    arr = []
    nPuppies = int(input("Number of puppies for User "+ str(num) +": "))
    for q in range(1,nPuppies + 1):
        x, y = input("Position of Puppy "+str(q)+": ").split()
        arr.append(int(x))
        arr.append(int(y))
    too_far = []
    for x in range(nPuppies):
        if (abs(arr[2 * x] - qx) + abs(arr[2*x + 1] - qy) > 10):
            too_far.append(str(x+1))
    if len(too_far) != []:
        for x in too_far:
            output = output + "Puppy " + str(x) + " (User " + str(num) + ") and " 
if output == "":
    print("No puppies too far away")
else:
    print(output[:-4:] + "too far away")
