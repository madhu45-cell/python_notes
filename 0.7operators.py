# Python Operators
'''Operators are used to perform operations on variables and values.'''
'''In the example below, we use the + operator to add together two values:'''
print(10 + 5) #15


# Python divides the operators in the following groups:
'''
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators (Its additional)
'''

# Python Arithmetic Operators
'''Arithmetic operators are used with numeric values to perform common mathematical operations:'''
'''
Operator	 Name
+	         Addition
-	         Subtraction
*	         Multiplication
/	         Division
%	         Modulus
**	         Exponentiation
//	         Floor division
eg.
'''
x = 6
y = 2
print(x+y) #8
print(x-y) #4
print(x*y) #12
print(x/y) #3.0
print(x%y) #0
print(x**y) #36
print(x//y) #3

# Python Assignment Operators
'''Assignment operators are used to assign values to variables:'''
'''
Operator   Example
=          x = 5
+=         x += 3	
-=         x -= 3	
*=         x *= 3	
/=         x /= 3	
%=         x %= 3	
**=        x **= 3	
//=        x //= 3	
'''


# Python Comparison Operators
'''Comparison operators are used to compare two values:'''
'''
Operator	Name
==	        Equal
!=	        Not equal
>	        Greater than
<	        Less than
>=	        Greater than or equal to
<=	        Less than or equal to
eg.
'''
a = 10
b = 5
c = 10
print(a==b) #False
print(a==c) #True
print(a!=b) #True
print(a!=c) #False
print(a>b) #True
print(a<b) #False
print(a<=b) #False
print(a>=b) #True
print(a<=c) #True


# Python Logical Operators
'''Logical operators are used to combine conditional statements:'''
'''
Operator	 Description	                                            Example
and 	     Returns True if both statements are true                   x < 5 and  x < 10
or	         Returns True if one of the statements is true	            x < 5 or x < 4
not	         Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
'''


# Python Identity Operators
'''Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:'''
'''
Operator	Description
is 	        Returns True if both variables are the same object
is not	    Returns True if both variables are not the same object
eg.
'''
w = 5
q = 5
e = 6
print(w is q) #True
print(w is not q) #False
print(w is e) #False
print(w is not e) #True



# Python Membership Operators
'''Membership operators are used to test if a sequence is presented in an object:'''
'''
Operator	Description
in 	        Returns True if a sequence with the specified value is present in the object
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y	

'''
o = [1,2,3,4]
g = 3
h = 9
print(g in o) #True
print(h in o) #False
print(g not in o) #False
print(h not in o) #True




# Operator Precedence
'''Operator precedence describes the order in which operations are performed.'''
'''The precedence order is described below, starting with the highest precedence at the top to bottom:
1st ()	            Parentheses
2nd **	            Exponentiation
3rd *  /  //  %	    Multiplication, division, floor division, and modulus
4th +  -	        Addition and subtraction
the same precedence, and therefore we evaluate the expression from left to right:
'''
print((6 + 3) - (6 + 3)) #0
print(5 + 4 - 7 + 3) #5