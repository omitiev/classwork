class A:


    def foo(self):
        print("I'm foo (A)")

    def __init__(self):
        self.attr1 = "attrA"

class A1(A):
    pass


class B(A):
    def foo(self):
        print("I'm foo (B)")

    def __init__(self):
        super().__init__()
        self.attr2 = "attrB"


class C(A):
    def foo(self):
        print("I'm foo (C)")

    def __init__(self):
        super().__init__()
        self.attr3 = "attrC"



class D(B,C):
    def foo(self):
        print("I'm foo (D)")

    def __init__(self):
        super().__init__()
        self.attr4 = "attrD"


b = B()
b.foo()
print(b.attr1)
print(b.attr2)
# print(B.mro())