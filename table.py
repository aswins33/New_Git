"""num=int(input("enter a number: "))
for i in range(1,11):
    table=num*i
    print(f"{num} * {i} = {table}")

    #(num,"*" ,i,"=",num*i)"""

import copy 
a=[[2,4,6],[54,33,87]]
b= copy.copy(a)

b[0][1]=10
print(a[0])