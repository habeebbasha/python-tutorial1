#FABONACCI NUMBERS BY USING GENERATOR FUNCTION\
# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    for i in range(0,limit+1):
        yield a
        a, b = b, a + b

    # Create a generator object
x = fib(7)
# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(7):
    print(i)

#GENERATOR EXPRESSION
generator=(num for num in range(10) if num%2==0)
for i in generator:
    print(i)