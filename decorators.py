def f1(str):
    def f2():
        return "welcome to "
    return f2()+str
def f3(sbr):
    return sbr
print(f1(f3("my code")))


#ABOVE EXAMPLE PROGRAM USING DECORATOR
def f1(fun):
    def f2(sbr):
        return "welcome to "+fun(sbr)
    return f2
@f1
def f3(sbr):
    return sbr
print(f3("my code"))