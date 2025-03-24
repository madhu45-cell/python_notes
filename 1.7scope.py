# Python Scope
'''In Python, scope refers to the visibility and accessibility of variables in different parts of the program.
Python has four types of scopes, often remembered by LEGB Rule.
'''
'''
LEGB Rule 
LEGB stands for:
Local (L) - Inside the current function.
Enclosing (E) - In the enclosing function (for nested functions).
Global (G) - Defined at the top level of the script/module.
Built-in (B) -  Predefined names in Python (e.g., print, len).
'''
# Global Scope
x = 10  # Global variable
def outer_function():
    # Enclosing Scope
    y = 20  
    def inner_function():
        # Local Scope
        z = 30  
        print(x)  # Accessing Global variable
        print(y)  # Accessing Enclosing variable
        print(z)  # Accessing Local variable
    inner_function()
outer_function()

# Local Scope
'''A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
'''
def myfunc():
  x = 300
  print(x)
print(x) #given error x not define
myfunc() #300

'''
Function Inside Function
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
'''
def myfunc():
  x = 300
  def myinnerfunc():
    print(x) #300
  myinnerfunc()
myfunc()


# Global Scope
'''
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.
'''
x = 300
def myfunc():
  print(x) #300
myfunc()
print(x) #300

# Naming Variables
'''
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
'''
'''The function will print the local x, and then the code will print the global x:'''
x = 300
def myfunc():
  x = 200
  print(x) #200
myfunc()
print(x) #300


# Global Keyword
'''
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.
'''
'''If you use the global keyword, the variable belongs to the global scope:
'''
x = 500
def myfunc():
  global x
  x = 600
  print(x) #600
myfunc()
print(x) #600


# Nonlocal Keyword
'''
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.
'''
'''If you use the nonlocal keyword, the variable will belong to the outer function:
'''
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x #hello
print(myfunc1())
