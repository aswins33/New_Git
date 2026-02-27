"""for num in range(3,8):
    fact = 1
    for k in range(1,num+1):
        fact = fact*k
        print(fact)
"""
  

"""name=input("enter your name: ")
for k in name:
       if k in "AEIOUaeiou":
              print(f"{k} = {d[k]}")"""


name=(input("enter your name: "))
d=dict()
for k in name:
    if k in "AEIOUaeiou":
        if k in d:
            d[k]=d[k]+1
        else:
            d[k]=1
for k in d:
    print(f"{k} = {d[k]}")