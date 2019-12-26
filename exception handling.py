#HANDLING OF ERRORS
def div(a,b):
    try:
        print(a/b)
    except Exception:
        print("you can't devide a number with zero")
    print('bye')
div(2,0)
#IN ANOTHER WAY
def divv(a,b):
    try:
        print("resource open")
        print(a/b)
    except Exception as e:#e as some reference
        print("hey!,u can't divide a number with zero (zero division error)")
    finally:
        print("resource closed")
divv(4,0)

#HANDLING WITH DIFFERENT ERRORS
def di(a,b):
    try:
        print("resource open")
        print(a/b)
        k=int(input("enter a number:"))
        print(k)
    except ZeroDivisionError as e:
        print("hey!,u can't devide a number by zero")
    except ValueError as e:
        print("invalid input")
    except Exception as e:
        print("something went wrong....")
    finally:
        print("resource closed")
di(4,2)

# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print
    "An exception"
    raise #'''To determine whether the exception was raised or not
              #here we get error bcoz raise at last'''














