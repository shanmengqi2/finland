class Shape ():
    def __init__(self,name,length) :
        self.name = name
        self.length = length
    
    def area(self):
        return 0
    

class Square (Shape):
    def __init__(self,name,length):
        # super(Square,self).__init__(name,length)
        super().__init__(name,length)
    
    def area(self):
        return self.length ** 2
    
    def describe(self):
        return self.name

s = Square('square',5)
print(s.area())
print("This ia a:",s.describe())
