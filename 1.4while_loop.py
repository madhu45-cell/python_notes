# Python While Loops
'''With the while loop we can execute a set of statements as long as a condition is true.
The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
while condidions:
    statements
    increments
'''
'''Print i as long as i is less than 6:
'''
i = 1
while i < 6:
  print(i)
  i += 1
# 1
# 2
# 3
# 4
# 5


# The break Statement
'''With the break statement we can stop the loop even if the while condition is true:'''
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# 1
# 2
# 3


# The continue Statement
'''With the continue statement we can stop the current iteration, and continue with the next:'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# 1
# 2
# 4
# 5
# 6


# The else Statement
'''With the else statement we can run a block of code once when the condition no longer is true:'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6

