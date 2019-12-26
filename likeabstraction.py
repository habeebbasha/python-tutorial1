#HIDING UNNECESSARY DETAILS FROM THE USER

from abc import ABC,abstractmethod
@abstractmethod
class animal(ABC):
    def move(self):
        self.s=2
        return print(self.s)
class human(animal):
    def move(self):
        print("i can walk...")
class snake(animal):
    def move(self):
        print("i can crawl..")
a=animal()
a.move()

#ANOTHER PROGRAM
from abc import ABC,abstractmethod
@abstractmethod
class university(ABC):
    def __init__(self,str):
        self.str=str
        return str
class institute(university):
    def __init__(self,rollno,str):
        super().__init__(str)
        self.rollno=rollno
    def getvalue(self):
        return print(self.rollno,self.str)
a=university("habeeb")
print(a)

