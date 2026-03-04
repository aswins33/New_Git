def mydecorator(fun):    # fun --> add
    def wrapper(a,b):
        if a>0 and b>0:
            fun(a,b)   # fun(1,3) --> add(1,3)
        else:
            print("number should be greater than 0 ")
    return wrapper
@mydecorator
def add(a,b):
    print(a+b)


my_fun=mydecorator(add) # my_fun --> add
my_fun(1,3)