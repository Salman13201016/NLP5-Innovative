


sample1 = "salman"
sample2 = [1,2,3,4]

print(len(sample1))
print(len(sample2))


#how to optimize the below code
class Car:
    def __init__(self,model):
        self.model = model
    def move(self):
        print("drive")
class Rickshaw:
    def __init__(self,model):
        self.model = model
    def move(self):
        print("paddle")

class Air:
    def __init__(self,model):
        self.model = model
    def move(self):
        print("fly")


car1 = Car("c1")
rick = Rickshaw("r1")
air = Air("a1")

for x in(car1,rick,air):
    x.move()