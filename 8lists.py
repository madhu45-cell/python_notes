# Python Lists
'''mylist = ["apple", "banana", "cherry"]
'''

# List
'''
Lists are used to store multiple items in a single variable.
List are mutable means change.
Lists are created using square brackets:
'''
thislist = ["apple", "banana", "cherry"]
print(thislist) #['apple', 'banana', 'cherry']

# List Items
'''List items are ordered, changeable, and allow duplicate values.'''
'''
Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
'''
'''
Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
'''
'''
Allow Duplicates
Since lists are indexed, lists can have items with the same value:
'''
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) #["apple", "banana", "cherry", "apple", "cherry"]


# List Length
'''To determine how many items a list has, use the len() function:'''
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #3

# List Items - Data Types
'''List items can be of any data type: String, int and boolean data types'''
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
'''A list can also contain different data types:'''
list1 = ["abc", 34, True, 40, "male"]

# type()
'''lists are defined as objects with the data type 'list':'''
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #<class 'list'>


# The list() Constructor
'''It is also possible to use the list() constructor when creating a new list.'''

thislist = list(("apple", "banana", "cherry"))
print(thislist) #['apple', 'banana', 'cherry']


# Access List Items
'''List items are indexed and you can access them by referring to the index number:
normal indexing start with 0(start) to ending point.
negative  indexing start with -1(end) to starting point
'''
thislist =     ["apple", "banana", "cherry"]
# idx             0          1         2           len = 3
# negative idx   -3         -2        -1
print(thislist[1]) #banana
print(thislist[-1]) #cherry


# Range of Indexes
'''You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# idx         0         1         2          3        4        5        6
# neg idx     -7        -6       -5         -4        -3       -2       -1
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']





# Change Item Value
'''To change the value of a specific item, refer to the index number:'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

# Change a Range of Item Values
'''o change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
'''If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
The length of the list will change when the number of items inserted does not match the number of items replaced.
'''
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']
'''If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:'''
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']



# Add List Items
# Append Items
'''To add an item to the end of the list, use the append() method:
list.append('item')
'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

# Insert Items
'''To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:
list.insert(idx, item)
'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #['apple', 'orange', 'banana', 'cherry']

# Extend List
'''To append elements from another list to the current list, use the extend() method.
The elements will be added to the end of the list.
list1.extend(list2)
'''
list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']




# Remove List Items
# Remove Specified Item
'''the remove() method removes the specified item.
list.remove(item)
'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']
'''If there are more than one item with the specified value, the remove() method removes the first occurrence: left to right
'''
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry', 'banana', 'kiwi']

# Remove Specified Index
'''The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.
list.pop() #remove last item
list.pop(index) #remove index item
'''
thislist = ["apple", "banana", "cherry"]
# idx         0         1          2
thislist.pop(1)
print(thislist) #['apple', 'cherry']
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']

# del keyword 
'''The del keyword also removes the specified index:
The del keyword can also delete the list completely.
del list #delete list
del list[index] #remove index item
'''
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']
thislist = ["apple", "banana", "cherry"]
# del thislist
print(thislist) # give NameError: name 'thislist' is not defined

# Clear the List
'''The clear() method empties the list.
The list still remains, but it has no content.
list.clear()
'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]


#Loop Lists
'''Loop Through a List
You can loop through the list items by using a for loop:
'''
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# apple
# banana
# cherry



# Sort Lists
# Sort List Alphanumerically
'''List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
list.sort()
'''
'''Sort the list alphabetically:
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']
'''Sort the list numerically:
'''
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #[23, 50, 65, 82, 100]

# Sort Descending
'''To sort descending, use the keyword argument reverse = True:
list.sort(reverse = True)
'''
'''Sort the list descending:
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #[100, 82, 65, 50, 23]


# Reverse Order
'''What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.
list.reverse()
'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']



# Copy a List
'''You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
'''
# Use the copy() method
'''You can use the built-in List method copy() to copy a list.'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #['apple', 'banana', 'cherry']
# Use the list() method
'''Another way to make a copy is to use the built-in method list().'''
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #['apple', 'banana', 'cherry']
# Use the slice Operator
'''You can also make a copy of a list by using the : (slice) operator.'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) #['apple', 'banana', 'cherry']


# Join Lists
'''Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator.
'''
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]
'''Another way to join two lists is by appending all the items from list2 into list1, one by one:'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1) #['a', 'b', 'c', 1, 2, 3]
'''Or you can use the extend() method, where the purpose is to add elements from one list to another list:'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]


# Multiply Lists
'''If you want to multiply the content of a Lists a given number of times, you can use the * operator:'''
fruits = ["apple", "banana", "cherry"]
myList = fruits * 2
print(myList) #['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']



# List Methods
'''
Method	      Description
append()	  Adds an element at the end of the list
clear()	      Removes all the elements from the list
copy()	      Returns a copy of the list
count()	      Returns the number of elements with the specified value
extend()	  Add the elements of a list (or any iterable), to the end of the current list
index()	      Returns the index of the first element with the specified value
insert()	  Adds an element at the specified position
pop()	      Removes the element at the specified position
remove()	  Removes the item with the specified value
reverse()	  Reverses the order of the list
sort()	      Sorts the list
'''