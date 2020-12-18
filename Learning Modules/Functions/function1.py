# File used to learn the useage of functions in Python 3
# Start date: 18/12/2020
# End date:
# by H Goodwin

# The def command defines the indented code as a function. This means the code will not be executed until the function is called.
# Functions can be used as many times as they are needed.
def function1():
    print("Print statement 1")
    print("Print statement 2")


# The following line of code is not indented withing the def and is therefore executed without calling function1
print("This is not inside the function")

# The following line calls function1, executing every line of code defined within the function
function1()

# a mapping
# a fucntion that takes an input/argument, x, and returns 2*x to the user


def function2(x):
    return 2*x


# The following line assigns the function "function2" to a with the argument 3 for x
a = function2(3)
print(a)


# Some examples of being able to call function2 multiple times with different arguments
a = function2(3)
print(a)
b = function2(14)
print(b)
c = function2(250)
print(c)

# Here is a function that takes 2 arguments, returning both arguments added together


def function3(x, y):
    return x + y


# Some examples of being able to call function3 multiple times with different arguments
a = function3(3, 4)
print(a)
b = function3(14, 27)
print(b)
c = function3(250, 1750)
print(c)


def function4(x):
    print(x)
    print("This string is still in function4")
    return 3*x


a = function4(4)
print(a)
