
















for g in range(3,8):
    f=1
    for k in range(1,g+1):
        f=f*k
    print("factorial=",f)


a=(input("enter string"))
d=dict()
for k in a:
    if k in "aeiouAEIOU":
        if k in d:
            d[k]=d[k]+1
        else:
            d[k]=1
for k in d:
    print(f"{k}={d[k]}")


'''def oddeven(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
oddeven(5)'''

def add(*args):
    s=0
    for n in args:
        s+=n
    return s
print(add(2,5,7))


            

    


