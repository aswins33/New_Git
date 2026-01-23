number=int(input("enter the number:"))
fact=1
for num in range(1,number+1):
    fact=fact*num
    print(fact)


number=[ 2,7,8]
for h in number:
    fact=1
    for h in range(1,h+1):
       fact=fact*h
    print(f"factorial of {h} = {fact} ")
