# Variables are containers for storing data values.

a = 24
b = 'madhusudan'

# casting - If you want to specify the data type of a variable, this can be done with casting.

a = int(24)
b = str('madhusudan')


# You can get the data type of a variable with the type() function.
a = 24
b = 'madhu'
print(type(a)) #<class 'int'>
print(type(b)) #<class 'str'>

# String variables can be declared either by using single or double quotes.
x = 'madhu'
y = "madhusudan"


# Variable names are case-sensitive. a and A both are diffrent.
a = 2
A = 3
print(a) #2
print(A) #3


# Legal variable names.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Illegal variable names.
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''



# Multi Words Variable Names
'''
Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:
'''
# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"
'''we use most of camel & snake case technique.'''




# Python allows you to assign values to multiple variables in one line.
x, y, z = "Orange", "Banana", "Cherry"

# And you can assign the same value to multiple variables in one line.
x = y = z = "Orange"
''' Make sure the number of variables matches the number of values, or else you will get an error.'''


# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x) #Python is awesome


