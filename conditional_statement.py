d1=int(input("enter the first number:"))
d2=int(input("enter the second number:"))

print("1.addition")
print("2.subtract")
print("3.multipication")
print("4.division")

choice=int(input("enter your choice(1/2/3/4): "))
if choice==1:
    print("addition is:", d1+d2)
elif choice==2:
    print("subtractin is:", d1-d2)
elif choice==3:
    print("multipication is:", d1*d2)
elif choice==4:
    print("dividion is:",d1/d2)
else:
    print("invalid output")