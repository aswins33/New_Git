
'''
for g in range(3,8):
    f=1
    for k in range(1,g+1):
        f=f*k
    print("factorial=",f)'''


'''a=(input("enter string"))
d=dict()
for k in a:
    if k in "aeiouAEIOU":
        if k in d:
            d[k]=d[k]+1
        else:
            d[k]=1
for k in d:
    print(f"{k}={d[k]}")
'''

'''def oddeven(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
oddeven(5)'''

'''def add(*args):
    s=0
    for n in args:
        s+=n
    return s
print(add(2,5,7))
'''


'''
character_count={}

word=input("Enter your word : ") 
for k in word:
    if k in "aeiouAEIOU":
        if k in character_count:
            character_count[k]=character_count[k]+1
        else:
            character_count[k]=1

print(character_count)         
'''
"""
1
2 3
4 5 6 
7 8 9 10

"""
'''line=6
num=1

for row in range(1,line +1):
    for c in range(row):
        print(num,end=" ")
        num+=1
    print("")'''

#factorial

num=1
while num<=7:

    c=1
    fact=1
    while c<=num:
        fact=fact*c
        c+=1
    print(fact)
    num+=1  

'''count=1
while count<=10:
    print(count,end=" ")
    count+=1'''

#prime numbers

arc=int(input("enter a number:" ))
if arc <=1:
    print("not prime number")
else:
    for c in range(2,arc):
        if arc%c==0:
            print("not prime number")
            break
    else:
        print("prime number")