num=int(input("enter a number:"))
if num <=1:
    print("prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("prime number")
            break
        else:
            print("not a prime number")
            break






mark=int(input("enter your mark:"))
if mark>=95:
    print("A+")
elif mark>=90:
    print("A")
elif mark>=85:
    print("B+")
elif mark>=80:
    print("B")
elif mark>=75:
    print("C+")
elif mark>=70:
    print("C")
else:
    print("fail")