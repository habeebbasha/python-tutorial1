class person:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemployee(self):
        return False
class employee(person):
    def __init__(self,name,eid):
        super().__init__(name)
        self.eid=eid
    def isemployee(self):
        return True
    def getid(self):
        return self.eid
a=employee("habeeb","1234")
print(a.getname(),a.isemployee(),a.getid())

#PREDICT THE FALLOWING OUTPUT

class X(object):
    def __init__(self, a):
        self.num = a

    def doubleup(self):
        self.num *= 2


class Y(X):
    def __init__(self, a):
        X.__init__(self, a)

    def tripleup(self):
        self.num *= 3
obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)
#ANOTHER PROGRAM



class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def getcar(self):
        return self.name,self.model
class bmw(car):
    def __init__(self,name,model,mil,eng):
        super().__init__(name,model)
        self.mil=mil
        self.eng=eng
    def getbmw(self):
        return self.mil,self.eng
a=bmw("bmw",2018,7,"200cc")
print(a.getcar(),a.getbmw())











0
