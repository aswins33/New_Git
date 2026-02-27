class A:
    def __init__(self):
        print("Hello aswin..")
        
class B:
    def __init__(self):
        C.__init__(self)
        print("hello tesna")
class C:
    def __init__(self):
        print("hELLO EBIN")

class D(B,C):
    pass

od=D()