"""
d=[2,3,5,7,4,]
for k in d:
    if k%2==0:
        print("the number is even")
    else:
        print("the number is odd")

"""

"""num=int(input("enter the number:"))
fact=1
for num in range(1,num+1):
    fact=fact*num
print(fact)"""

"""text = "aswin sivadas"

for char in text:
    print(char)"""

text=(input("enter the string:"))
d={}

for char in text:
  if char in "AEIOUaeiou":
        if char in d:
            d[char]=d[char]+1
        else:
            d[char]=1
for char in d:
    print(char," = ",d[char])