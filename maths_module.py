def is_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    

def fatorial(num):
    fact=1
    for k in range(1,num+1):
        fact=fact*k
    return fact