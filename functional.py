numbers=[12,45,2,7]

def multiply(num):
    return num*2
m=list(map(multiply,numbers))
print(m)


arc=[12,45,2,7]

n = list(map(lambda num:num*2,arc))
print(n)

l=list(filter(lambda num:num%2==0,arc))
print(l)