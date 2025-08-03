class USER:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        print(f"this is {self.name} & email is {self.email}")

class Customer(USER):
    def __init__(self,name,email,address):
        super().__init__(name,email)

        print("this is constructor B")

class C(Customer):
    pass
a = USER('salman','salmanmdsultan@gmail.com')

b = Customer('salman1','salmanmdsultan@gmail1.com','Mirpur')


