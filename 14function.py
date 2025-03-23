# Python Functions
'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''

# Creating a Function
'''In Python a function is defined using the def keyword:
def functionName():
    block of code
'''
def my_function():
  print("Hello from a function")

# Calling a Function
'''To call a function, use the function name followed by parenthesis:
functionName()
'''
def my_function():
  print("Hello from a function")
my_function() #Hello from a function


# Parameters or Arguments?
'''Parameters are the variables defined in a function declaration. Inside the function definition.
Arguments are the actual values passed to a function when calling it. Inside the function call.
def functionName(parameters):
    do some task
functionName(Arguments)
'''
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil") #Emil Refsnes
my_function("Tobias") #Tobias Refsnes
my_function("Linus") #Linus Refsnes

# Number of Arguments
'''By default, a function must be called with the correct number of arguments.
 Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
'''
'''The function expects 2 arguments, and gets 2 arguments:
If you try to call the function with 1 or 3 arguments, you will get an error:
'''


# Arbitrary Arguments, *args
'''If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
'''
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") #The youngest child is Linus


# Keyword Arguments
'''You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #The youngest child is Linus


# Arbitrary Keyword Arguments, **kwargs
'''If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes") #His last name is Refsnes



# Default Parameter Value
'''The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:
'''
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden") #I am from Sweden
my_function("India") #I am from India
my_function() #I am from Norway
my_function("Brazil") #I am from Brazil



# Return Values
'''To let a function return a value, use the return statement:
return are the end of function, after return no line of code is work.
'''
def my_function(x):
  return 5 * x
  print(x)
print(my_function(3)) #15
print(my_function(5)) #25
print(my_function(9)) #45


# Recursion in Python
'''
Recursion is a programming technique where a function calls itself to solve a smaller instance of the original problem. It is useful for problems that can be broken down into smaller subproblems of the same type.
'''
'''The factorial of a number n is defined as:'''
def factorial(n):
    if n == 0: 
        return 1
    else:
        return n * factorial(n - 1) 

print(factorial(5)) #120




# Python Lambda
'''A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
use for Short, one-line functions
'''
'''
Syntax
lambda arguments : expression
'''

'''Add 10 to argument a, and return the result:'''
x = lambda a : a + 10
print(x(5)) #15

'''Multiply argument a with argument b and return the result:'''
x = lambda a, b : a * b
print(x(5, 6)) #30

'''
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
Use lambda functions when an anonymous function is required for a short period of time.
'''
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) #22


