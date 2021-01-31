isbn = input("ISBN: ")
sum = 0
isbn_ldr = isbn[:-1:] #ISBN Last Digit Removed
isbn_w1 = isbn_ldr[::2] #ISBN number that have weight 1
isbn_w3 = isbn_ldr[1::2] #ISBN number that have weight 3
for i in isbn_w3:
    sum += int(i)*3
for i in isbn_w1:
    sum += int(i)
if 10 - int(int(isbn[12])) == 10:
    cd = 0
else:
    cd = 10 - int(isbn[12])
if sum % 10 == cd:
    print("Valid")
else:
    print("Invalid")