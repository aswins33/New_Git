num=int(input("enter the  number : "))
start=int(input("enter the first number : "))
end=int(input("enter the ending number : "))

print(f"Numbers which are divisible by {num} are : ")
for h in range(start,end+1):
    if h%num==0:
        print(h,end=" ")

        