class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__() 
#super_Follows_MRO = Method Resolution Order
#MRO = C3 Linearization method
d = D() #D->B->C->A

#starts with D
#then go to the B 
#Theb check B's Parent(A)
#then check C
#then check A
print(D.__mro__)

#how MRO Works
#how l3 linearization works
#why do we need MRO