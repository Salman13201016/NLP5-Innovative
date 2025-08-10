
class myIterator:
    def __init__(self,data):
        print("3")
        self.data = data
        self.index = 0
    def __next__(self):
        if self.index<len(self.data):
            print("4")
            result = self.data[self.index]
            self.index=self.index+1
            return result
        else:
            print("5")
            raise StopIteration

class MyIterable:
    def __init__(self,data):
        print("1")
        self.data = data
        
    def __iter__(self):
        
        print("2")
        return myIterator(self.data)

my_iterable = MyIterable([10,20,30])
for i in my_iterable:
    print(i)