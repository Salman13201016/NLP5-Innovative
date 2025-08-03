class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        print("B init")
        A.__init__(self)

class C(A):
    def __init__(self):
        print("C init")
        A.__init__(self)

class D(B, C):
    def __init__(self):
        print("D init")
        B.__init__(self)
        C.__init__(self)
d = D()