"""
number=int(input("enter a number:"))
if number <=1:
    print("not a prime number")

else:
    for k in range(2,number):
        if number % k ==0:
            print("not a prime number")
            break
    else:
        print("prime number")


"""


h=(24,16,11,33,31,20)
for a in h:
    if a <=1:
        pass
    else:
        for b in range(2,a):
             if a%b == 0:
                  break
        else:
            print(a)


f=(11,13,15,17,19,21,24,26,22,30)
for kav in f:
    if kav <=1:
        pass
    else:
        for ash in range(2,kav):
            if kav%ash == 0:
                  break
        else:
            print(kav,end=" ")
