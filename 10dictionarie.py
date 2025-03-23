# Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Dictionary
'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# Dictionary Items
'''Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) #ford 
'''Ordered or Unordered?
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
'''
'''Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
'''
'''Duplicates Not Allowed
Dictionaries cannot have two items with the same key:, but they have same value in diffrent key.
'''
'''Duplicate values will overwrite existing values:'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Dictionary Length
'''To determine how many items a dictionary has, use the len() function:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict)) #3


# Dictionary Items - Data Types
'''The values in dictionary items can be of any data type: String, int, boolean, and list data types:
'''
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# type()
'''dictionaries are defined as objects with the data type 'dict':'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) #<class 'dict'>


# The dict() Constructor
'''It is also possible to use the dict() constructor to make a dictionary.
'''
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) #{'name': 'John', 'age': 36, 'country': 'Norway'}


# Accessing Items
'''You can access the items of a dictionary by referring to its key name(indexing not allowde), inside square brackets:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"]) #Mustang

'''there is also a method called get() that will give you the value of key:
dict.get(key)
'''
print(thisdict.get("model")) #Mustang


# Get Keys
'''The keys() method will return a list of all the keys in the dictionary.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys()) #dict_keys(['brand', 'model', 'year'])

# Get Values
'''The values() method will return a list of all the values in the dictionary.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.values()) #dict_values(['Ford', 'Mustang', 1964])

# Get Items
'''The items() method will return each item in a dictionary, as tuples in a list. Get a list of the key:value pairs
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.items()) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# Change Dictionary Items
'''Change Values
You can change the value of a specific item by referring to its key name:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Update Dictionary
'''The update() method will update the dictionary with the items from the given argument. If the item does not exist, the item will be added.
The argument must be a dictionary, or an iterable object with key:value pairs.
dict.update(argument)
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Add Dictionary Items
'''Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# Remove Dictionary Items
'''Removing Items
There are several methods to remove items from a dictionary:
'''
'''The pop() method removes the item with the specified key name:
dict.pop(keyName) 
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) #{'brand': 'Ford', 'year': 1964}

'''The popitem() method removes the last inserted item: takes no arguments
dict.popitem() 
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang'}

'''The del keyword removes the item with the specified key name: they do same like pop() method.
del dict[keyName]
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) #{'brand': 'Ford', 'year': 1964}
'''The del keyword can also delete the dictionary completely:'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# del thisdict
print(thisdict) #NameError: name 'thisdict' is not defined.

'''The clear() method empties the dictionary:'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) #{}


# Loop Through a Dictionary
'''Print all key names in the dictionary, one by one:, by loop'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
# brand
# model
# year

'''Print all values in the dictionary, one by one:'''
for x in thisdict:
  print(thisdict[x])
# Ford
# Mustang
# 1964

'''You can also use the values() method to return values of a dictionary:'''
for x in thisdict.values():
  print(x)
# Ford
# Mustang
# 1964
'''You can use the keys() method to return the keys of a dictionary:'''
for x in thisdict.keys():
  print(x)
# brand
# model
# year
'''Loop through both keys and values, by using the items() method:'''
for x, y in thisdict.items():
  print(x, y)
# brand Ford
# model Mustang
# year 1964


# Copy a Dictionary
'''You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
 and changes made in dict1 will automatically also be made in dict2.
'''
'''There are ways to make a copy, one way is to use the built-in Dictionary method copy().
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
'''Another way to make a copy is to use the built-in function dict().
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Nested Dictionaries
'''A dictionary can contain dictionaries, this is called nested dictionaries.'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

'''Create three dictionaries, then create one dictionary that will contain the other three dictionaries:'''

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Access Items in Nested Dictionaries
'''To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"]) #Tobias




# Dictionary Methods
'''
Method	         Description
clear()	         Removes all the elements from the dictionary
copy()	         Returns a copy of the dictionary
fromkeys()	     Returns a dictionary with the specified keys and value
get()	         Returns the value of the specified key
items()	         Returns a list containing a tuple for each key value pair
keys()	         Returns a list containing the dictionary's keys
pop()	         Removes the element with the specified key
popitem()	     Removes the last inserted key-value pair
setdefault()	 Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	     Updates the dictionary with the specified key-value pairs
values()	     Returns a list of all the values in the dictionary
'''