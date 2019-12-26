
class add:
    def __init__(self,a,b):  #this is a constructor
        self.a=a
        self.b=b
    def ope(self):
        add= self.a+self.b
        return add
s=add(2,3)
print(s.ope())
#THIS IS AN EXAMPLE PROGRAM OF GET AND SET OF VALUES
class info:
    def getinf(self,name,age):
        self.name=name
        self.age=age
    def setinf(self):
        return self.name,self.age
a=info()
a.getinf("habeeb",22)
print(a.setinf())