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
2myvar = "John"
my-var = "John"
my var = "John"