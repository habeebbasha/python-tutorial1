
#encapsulation means ristricting of methods and variables
class mobile:
    def __init__(self):
        self.__updatesoftware()   #private method(private means which can't changable)
    def memory(self,size):
        self.size=size
    def __updatesoftware(self): #private method(private means which can't changable)
        print("alreay updated.")
a=mobile()

#private variables(private means which can't changble)

class laptop:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed=200
        self.__name="BMW"
    def fuel(self):
        print("fuel is full..")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)
laptop_obj=laptop()
laptop_obj.fuel()
laptop_obj.setspeed(100)



