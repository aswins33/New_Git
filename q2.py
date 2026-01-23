
"""
name=input("enter the name:")
age=input("enter your age")
print("hello",name, )
"""



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