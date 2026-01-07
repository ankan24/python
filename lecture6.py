# Functions and Recursion in Python
# This script demonstrates how to define and use functions in Python,
# including examples of recursion.

# Function - A block of reusable code that performs a specific task.
# def - keyword to define a function
# Function Definition
def cal_sum(a,b): # (Parameters received)
    """This function returns the sum of two numbers."""
    sum = a+b 
    print(sum) 
    return sum 
# Function Call (Arguments passed)
result = cal_sum(5, 10)
print("Sum:", result)



def hello() :
    print("Hello, World!") # this function will return value None

hello()  # Calling the function
hello()
hello()



# functions are two types :
# 1. Built-in functions : pre-defined functions in python like print(), len(), type() etc.
# 2. User-defined functions : functions defined by the user using def keyword like above cal_sum() and hello() functions.
print("Ankan", end="24")
print("Ghorai")


# default parameters
def cal_product(a, b=2): # b has a default value of 2
    """This function returns the product of two numbers."""
    product = a * b
    return product
print(cal_product(5))  # b will take the default value 2
print(cal_product(5, 3))  # b will take the value 3 passed      




# Recursion - A function that calls itself
def factorial(n):
    """This function returns the factorial of a number using recursion."""
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
    
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of 7:", factorial(7))
print("Recursion Example Complete")

# Note: Be cautious with recursion as it can lead to stack overflow if the base case is not defined properly.
# Call stack - the sequence of function calls that leads to a particular point in the program execution.
# Each time a function is called, a new layer is added to the call stack.
# When a function returns, its layer is removed from the stack.
# Maximum recursion depth - Python has a limit on the maximum depth of recursion to prevent infinite recursion.
# You can check or set this limit using sys module (import sys; sys.getrecursion
#limit() and sys.setrecursionlimit(limit)).


