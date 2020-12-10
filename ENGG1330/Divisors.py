input_incorr1 = True
input_incorr2 = True
outp = "M "
e = []
while input_incorr1:
    a, b = [int(x) for x in input("a b: ").split()]
    if a>0 and b>0:
        if b > a:
            input_incorr1 = False
while input_incorr2:
    d = [int(x) for x in input("Divisors: ").split()]
    all_clear = True
    for x in d:
        if x > b or not x>0:
            all_clear = False
    if all_clear:
        input_incorr2 = False
for x in d:
    if not x in e:
        e.append(x)
e.sort()
for x in e:
    outp += str(x) + " "
print(outp[:-1:])
for x in range(a, b):
    outp = str(x) + " "
    for i in e:
        if x % i == 0:
            outp += "1 "
        else:
            outp += "0 "
    print(outp[:-1:])
