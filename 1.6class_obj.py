# Python Classes and Objects
'''
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
'''
# Create a Class
'''To create a class, use the keyword class:'''
class MyClass:
  x = 5
print(MyClass) #<class '__main__.MyClass'>

# Create Object
'''Now we can use the class named MyClass to create objects:'''
p1 = MyClass()
print(p1.x) #5


# The __init__() Function
'''
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
'''
'''Create a class named Person, use the __init__() function to assign values for name and age:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name) #john
print(p1.age) #36


# Object Methods
'''
Objects can also contain methods. Methods in objects are functions that belong to the object.
Let us create a method in the Person class:
'''
'''Insert a function that prints a greeting, and execute it on the p1 object:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
print(p1) #<__main__.Person object at 0x102f2ae40>
p1.myfunc() #Hello my name is John

# The self Parameter
'''The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.'''
'''It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:'''

# Modify Object Properties
'''You can modify properties on objects like this:'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age) #40

# Delete Object Properties
'''You can delete properties on objects by using the del keyword:'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
# del p1.age
print(p1.name) #v
print(p1.age) #AttributeError: 'Person' object has no attribute 'age'

# Delete Objects
'''You can delete objects by using the del keyword:'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
# del p1
print(p1) #NameError: name 'p1' is not defined































