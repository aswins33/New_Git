class A:
    def methodA(self):
        self.a=10
class B(A):
    def methodB(self):
        self.b=20

class C(B):
    def methodC(self):
        print(self.a+self.b)

oc=C()
oc.methodA()
oc.methodB()
oc.methodC()