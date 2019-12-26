#DEFAULT CONSTRUCTOR(NO ARGUMENTS)
class GeekforGeeks:
    geek = ""

    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)

    # creating object of the class


obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()


#CONSTRUCTOR WITH ARGUMENTS
class cont:
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        self.final = self.first + self.second
        print(self.first,self.second)
        print(self.final)
obj=cont(100,200)
obj.display()