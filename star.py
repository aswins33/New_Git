
for row in range(1,7):
    for star in range(row):
        print("*",end=" ")
    print("")



for row in range(1,6):
    for num in range(1,row+1):
        print(num,end=" ")
    print("")


num=1
for row in range(1,2):
    for c in range(1,row+1):
     print(num)




for row in range(1,8):
    for a in range (1,row+1):
        print(row*a,end=" ")
    print("")



rows=6

for p in range(1,rows+1):
    print(" "*(rows-p)+"*"*p)



rows=5

for p in range(1,rows+1):
    for vpn in range(rows-p):
        print(" ",end="")
    for apn in range(p):
        print("*",end="")
    print("")