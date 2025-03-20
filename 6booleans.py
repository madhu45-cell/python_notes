# Python Booleans
'''Booleans represent one of two values: True(1) or False(0).
When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

'''The bool() function allows you to evaluate any value, and give you True or False in return,
'''

'''Most Values are True'''
print(bool("Hello")) #True
print(bool(15)) #True
print(bool(["apple", "cherry", "banana"])) #True

'''Some Values are False'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
