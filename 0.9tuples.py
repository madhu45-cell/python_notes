# Python Tuples
mytuple = ("apple", "banana", "cherry")

# Tuple
'''Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable(immutable).
Tuples are written with round brackets.
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')


# Tuple Items
'''Tuple items are ordered, unchangeable, and allow duplicate values.
'''
'''Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
'''
'''Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
'''
'''Allow Duplicates
Since tuples are indexed, they can have items with the same value:
'''
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #("apple", "banana", "cherry", "apple", "cherry")

# Tuple Length
'''To determine how many items a tuple has, use the len() function:'''
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #3

# Create Tuple With One Item
'''To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
'''
# this is a tuple.
thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>
#this is NOT a tuple.
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>


# Tuple Items - Data Types
'''Tuple items can be of any data type:
String, int and boolean data types:
A tuple can contain different data types:
'''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")



# type()
'''tuples are defined as objects with the data type 'tuple':'''
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #<class 'tuple'>



# The tuple() Constructor
'''It is also possible to use the tuple() constructor to make a tuple.'''
thistuple = tuple(["apple", "banana", "cherry"]) 
print(thistuple) #('apple', 'banana', 'cherry')





# Access Tuple Items
'''You can access tuple items by referring to the index number, inside square brackets:
normal indexing start with 0(start) to ending point.
negative  indexing start with -1(end) to starting point
'''
thistuple = ("apple", "banana", "cherry")
# idx          0         1          2
# neg idx     -3        -2         -1
print(thistuple[1]) #banana
print(thistuple[-1]) #cherry

# Range of Indexes
'''You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.
'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# idx          0         1         2         3        4        5        6 
# neg idx     -7        -6        -5        -4       -3       -2       -1
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:]) #('cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')

# Update Tuples
'''Tuples are unchangeable(immutable), meaning that you cannot change, add, or remove items once the tuple is created.
But there are some workarounds.
'''
# Change Tuple Values
'''Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #('apple', 'kiwi', 'cherry')

# Add Items to tuples
'''Convert the tuple into a list, add "orange", and convert it back into a tuple:'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')
'''Create a new tuple with the value "orange", and add that tuple:'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

# Remove Items
'''Convert the tuple into a list, remove "apple", and convert it back into a tuple:'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')

# delete the tuple
'''The del keyword can delete the tuple completely:'''
thistuple = ("apple", "banana", "cherry")
# del thistuple
print(thistuple) #give NameError: name 'thislist' is not defined



# Unpacking a Tuple
'''When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
'''
fruits = ("apple", "banana", "cherry")
print(fruits) #('apple', 'banana', 'cherry')

'''But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
Unpacking a tuple:
'''
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) #apple
print(yellow) #banana
print(red) #cherry


'''If the number of variables is less than the number of values, they can given error'''
fruits = ("apple", "banana", "cherry", "orange")
# (green, yellow, red) = fruits
# print(green) #ValueError: too many values to unpack (expected 3)
# print(yellow)
# print(red)
'''If the number of variables is more than the number of values, they can given error'''
fruits = ("apple", "banana")
# (green, yellow, red) = fruits
# print(green) #ValueError: not enough values to unpack (expected 3, got 2)
# print(yellow)
# print(red)

# Using Asterisk*
'''If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) #apple
print(yellow) #banana
print(red) #['cherry', 'strawberry', 'raspberry']
(green, *tropic, red) = fruits
print(green) #apple
print(tropic) #['banana', 'cherry', 'strawberry']
print(red) #raspberry



# Loop Through a Tuple
'''You can loop through the tuple items by using a for loop.
'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# apple
# banana
# cherry


# Join Tuples
'''Join Two Tuples
To join two or more tuples you can use the + operator:
'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) #('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
'''If you want to multiply the content of a tuple a given number of times, you can use the * operator:'''
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


# Tuple Methods
'''
Method	     Description
count()	     Returns the number of times a specified value occurs in a tuple
index()	     Searches the tuple for a specified value and returns the position of where it was found
'''