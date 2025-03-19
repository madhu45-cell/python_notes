# Strings
'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello"
You can display a string literal with the print() function:
'''

# Quotes Inside Quotes
'''You can use quotes inside a string, as long as they don't match the quotes surrounding the string:'''
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')



# Multiline Strings
'''You can assign a multiline string to a variable by using three double quotes or single quotes:'''
a = """Lorem ipsum dolor sit """
print(a)


# Looping Through a String
'''Since strings are arrays, we can loop through the characters in a string, with a for loop.'''
for x in "banana":
  print(x)


# String Length
'''To get the length of a string, use the len() function.'''
a = "Hello, World!"
print(len(a)) #13


# Check String
'''To check if a certain phrase or character is present in a string, we can use the keyword in.'''
txt = "The best things in life are free!"
print("free" in txt) #True

'''To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.'''
txt = "The best things in life are free!"
print("free" not in txt) #False



# String Slicing

'''they give us strings of given index'''
a = "Hello, World!"
#idx 0123456789012
 #  -12   to    -1
print(a[1]) #e

# Slicing.
'''You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string with end index not included. return end -1.
eg. b[2:5] - this means return the string from 2 index to 5-1(4) index.
'''
'''Get the characters from position 2 to position 5 (not included):'''
b = "Hello, World!"
print(b[2:5]) #llo

# Slice From the Start
'''By leaving out the start index, the range will start at the first character:
Get the characters from the start to position 5 (not included):
'''
b = "Hello, World!"
print(b[:5]) #Hello

# Slice To the End
'''By leaving out the end index, the range will go to the end:
Get the characters from position 2, and all the way to the end:
'''
b = "Hello, World!"
print(b[2:]) #llo, World!

# Negative Indexing
'''Use negative indexes to start the slice from the end of the string:

Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
    consider o [-5] to l [-2-1(-3)]
'''
b = "Hello, World!"
print(b[-5:-2]) #orl



# Modify Strings
'''Python has a set of built-in methods that you can use on strings.'''

# Upper Case
'''The upper() method returns the string in upper case:
'''
a = "Hello, World!"
print(a.upper()) #HELLO, WORLD!
# Lower Case
'''The lower() method returns the string in lower case:
'''
a = "Hello, World!"
print(a.lower()) #hello, world!
# Remove Whitespace
'''The strip() method removes any whitespace from the beginning or the end:
'''
a = " Hello, World! "
print(a.strip()) #Hello, World!


# String Concatenation
'''To concatenate, or combine, two strings you can use the + operator.
Merge variable a with variable b into variable c:
'''
a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld


# String Format
'''As we learned in the Python , we cannot combine strings and numbers like this: "hello" + 7.
But we can combine strings and numbers by using f-strings or the format() method!
'''
'''F-Strings
To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for can contain variables, operations, functions, and modifiers to format the value.
'''
age = 36
txt = f"My name is John, I am {age}"
print(txt) #My name is John, I am 36


# Escape Character
'''To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
'''
'''You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."
'''
'''To fix this problem, use the escape character \":
The escape character allows you to use double quotes when you normally would not be allowed:
'''
txt = "We are the so-called \"Vikings\" from the north."


# String Methods
'''
Method	               Description
capitalize()     	Converts the first character to upper case
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()        	Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()   	Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()             Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
'''