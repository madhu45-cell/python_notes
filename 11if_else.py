# Python Conditions and If statements
'''Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
'''
# Indentation
'''Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
If statement, without indentation (will raise an error):
'''

# if
'''An "if statement" is written by using the if keyword.
if conditions:
   statements
'''
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Elif
'''The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
if conditions:
   statements
elif condition:
   statements
'''
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") # print this condition

# Else
'''The else keyword catches anything which isn't caught by the preceding conditions.
if conditions:
   statements
elif condition:
   statements
else:
   statements
'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") # print this condition

'''You can also have an else without the elif:
if ----- starting 
else --- ending 
After else condition we cant take elif condition, If take then given error.
'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") # print this condition


# Short Hand If
'''If you have only one statement to execute, you can put it on the same line as the if statement.'''
if a > b: print("a is greater than b")
# Short Hand If ... Else
'''If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:'''
print("A") if a > b else print("B")

'''
This technique is known as Ternary Operators, or Conditional Expressions.
'''

# Nested If
'''You can have if statements inside if statements, this is called nested if statements.
'''
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# The pass Statement
'''if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.'''
a = 33
b = 200
if b > a:
  pass


